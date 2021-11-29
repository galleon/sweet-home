import pandas as pd
import tempfile

from bicoque.data import get_data


def dataframe():
    """
    Return a pandas dataframe with the following columns:
        'Id', 'YrSold', 'MoSold', 'SalePrice'
    """
    return pd.DataFrame(
        {
            "Id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "YrSold": [1925, 1925, 1925, 1925, 1925, 1925, 1925, 1925, 1925, 1925],
            "MoSold": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "SalePrice": [
                100000,
                200000,
                300000,
                400000,
                500000,
                600000,
                700000,
                800000,
                900000,
                1000000,
            ],
        }
    )


def test_get_data():
    df_created = dataframe()
    # create a temporary file
    with tempfile.NamedTemporaryFile() as f:
        df_created.to_csv(f.name, index=False)
        # read the data
        df_read = get_data(None, f.name)
        assert df_read.shape == (10, 4)
