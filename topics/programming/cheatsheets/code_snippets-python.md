  # Python Code Snippets

### Conda
`conda create --name myproject` create a new environment  
`conda remove --name myproject` delete an environment  
`conda activate myproject` activate a new environment  
`conda install <package-name>`  
`conda search <package-name>`  
`conda create --name new_name --clone old_name` clone an environment  
`conda remove --name old_name --all` delete everything associated with an old environment  
`conda env export > environment.yaml` export environment to a yaml file for easy sharing  
`conda env create -f environment.yaml` create an environment from a yaml file  


### Jupyter
`jupyter notebook list` list currently running jupyter instances  
`jupyter notebook stop <8888>` stop a running jupyter instance  

```python
from IPython.display import display, HTML, Markdown
display(HTML("<style>.container { width:95% !important; }</style>"))
```
^ make wide; also allow for Markdown display in cell output

**add to .gitignore:**
```
.ipynb_checkpoints
*/.ipynb_checkpoints/*
```

### Pandas
`df.rename(columns=str.lower)` lowercase all column names.  
`pd.set_option('display.float_format', lambda x: '%.5f' % x)` suppress scientific notation

```python
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
```


### Other Python

#### JSON
read json
```python
  with open('sample.json', 'r') as f:
      some_dict = json.load(f)
```

write json
```python
with open("sample.json", "w") as f:
    json.dump(some_dict, f)

```

#### YAML
```python
with open(self.config_yaml_path) as f:
    self.config_dict = yaml.safe_load(f)
```


#### import a custom python file from another directory
```python
import sys
sys.path.insert(1, '/path/to/file')
import somefile
```

#### Error handling
```python
try:
    func()
except AssertionError as error:
    print(error)
    print('The function was not executed')
```
