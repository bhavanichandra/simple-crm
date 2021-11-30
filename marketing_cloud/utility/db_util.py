import os

from mongoengine import connect
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

MONGO_CONNECTION_STR = str(os.getenv('MONGO_CONNECTION_STR'))
MONGO_DATABASE = str(os.getenv('MONGO_DATABASE'))


def response_wrapper(is_success: bool = False, message: str = "", data=None) -> dict[str, any]:
    """
    Wrapper for the response.
    :param is_success: True if the request was successful, False otherwise
    :param message: Message to be returned
    :param data: Data to be returned
    :return: Dict of the parameters
    """
    if data is None:
        data = {}
    return {
        "success": is_success,
        "message": message or "Unexpected error occurred.",
        "data": data
    }


class DatabaseAdapter:

    def __init__(self):
        self.client: MongoClient = connect(db=MONGO_DATABASE, host=MONGO_CONNECTION_STR)
        self.session = self.client.start_session()

    def execute_transaction(self, execute_function, *args, **kwargs):
        """
        Execute a function with the database connection
        """
        result = None
        while True:
            try:
                result = execute_function(session=self.session, *args, **kwargs)
                self._commit_transaction()
                break

            except (ConnectionFailure, OperationFailure) as ex:
                if ex.has_error_label('TransientTransactionError'):
                    continue
                else:
                    raise
        return result

    def _commit_transaction(self):
        """
        Commit the transaction. If error occurs, rollback the transaction
        """
        while True:
            try:
                self.session.commit_transaction()
                break
            except (ConnectionFailure, OperationFailure) as ex:
                if ex.has_error_label("UnknownTransactionCommitResult"):
                    print(
                        "UnknownTransactionCommitResult, retrying commit operation ...")
                    continue
                else:
                    print("Error during commit ... Stopping transaction")
                    raise
