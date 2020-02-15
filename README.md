# FunctionParallelProcessing


## Usage

```Python
from parallel_process_func import parallel_process_func

def x():
	print('-- x() START --')
	[i for i in range(10000000)]
	print('-- x() END --')

def y():
	print('-- y() START --')
	[i for i in range(10000000)]
	print('-- y() END --')

parallel_process_func(x, y) # 関数xと関数yの並列処理
# -- x() START --
# -- y() START --
# -- x() END --
# -- y() END --
```

## Run

```sh
pipenv run start # main.pyの実行
```
