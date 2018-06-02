import boto3
from boto3.dynamodb.conditions import Key

# TODO -> vir do conf
# better to use python-decouple or environment variables.
aws_access_key_id = 'yoursecretkey'
aws_secret_access_key = 'youraccesskey'


class DynamoDBInstance(object):
    def __init__(self, table_name, *args, **kwargs):
        self.session = self.init_session()
        self.dynamodb_resource = self.session.resource('dynamodb')
        self.table_name = table_name

    def init_session(self):
        return boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name='us-east-1'
        )

    def get_table_metadata(self):
        """
        Get some metadata about chosen table.
        """
        table = self.dynamodb_resource.Table(self.table_name)

        return {
            'num_items': table.item_count,
            'primary_key_name': table.key_schema[0],
            'status': table.table_status,
            'bytes_size': table.table_size_bytes,
            'global_secondary_indices': table.global_secondary_indexes
        }

    def read_table_item(self, pk_name, pk_value):
        """
        Return item read by primary key.
        """
        table = self.dynamodb_resource.Table(self.table_name)
        response = table.get_item(Key={pk_name: pk_value})

        return response

    def add_item(self, col_dict):
        """
        Add one item (row) to table. col_dict is a dictionary {col_name: value}.
        """
        table = self.dynamodb_resource.Table(self.table_name)
        response = table.put_item(Item=col_dict)

        return response

    def delete_item(self, pk_name, pk_value):
        """
        Delete an item (row) in table from its primary key.
        """
        table = self.dynamodb_resource.Table(self.table_name)
        table.delete_item(Key={pk_name: pk_value})

        return

    def scan_table(self, filter_key=None, filter_value=None):
        """
        Perform a scan operation on table.
        Can specify filter_key (col name) and its value to be filtered.
        """
        table = self.dynamodb_resource.Table(self.table_name)

        if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = table.scan(FilterExpression=filtering_exp)
        else:
            response = table.scan()

        return response

    def query_table(self, filter_key=None, filter_value=None):
        """
        Perform a query operation on the table.
        Can specify filter_key (col name) and its value to be filtered.
        """
        table = self.dynamodb_resource.Table(self.table_name)

        if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = table.query(KeyConditionExpression=filtering_exp)
        else:
            response = table.query()

        return response
