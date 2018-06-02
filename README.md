# Dynamodb Wrapper

This class was inspired by this shared [gist](https://gist.github.com/martinapugliese/cae86eb68f5aab59e87332725935fd5f)
I found it when i was needing some operations, and decided to write a small class to make easy for me to access all the functions.

#### You need to configure AWS_KEY and AWS_SECRET at the wrapper.py file

## Usage
Create an instance of the class
```python
from DynamoWrapper.wrapper import DynamoDBInstance

mytable = DynamoDBInstance('mydynamodbtable')
myitem = mytable.read_table_item('definedTableKey', value)
print(myitem)
```
