"""FlexIO package"""

from pathlib import Path

from src.Puffin.enums import FileType, VarType
from src.Puffin.DatasetConfig import FileDatasetConfig 
from src.Puffin.DatasetLibrary import DatasetLibrary 



if __name__ == "__main__":
    file_data_config = FileDatasetConfig(
        name = 'train_in',
        path = Path('data/test.csv'),
        filetype = FileType.csv,
        vartype = VarType.df,
    )

    dsl = DatasetLibrary()
    dsl.add_dataset_config(file_data_config)
    df = dsl.load('train_in')
    df


