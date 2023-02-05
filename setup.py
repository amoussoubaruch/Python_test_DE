from setuptools import setup, find_packages

setup(
    name='Python_test_DE',
    version='0.1',
    packages=find_packages(),
    install_requires=
        [
           "google-cloud-bigquery==1.26.0",    # For BigQuery 
           "google.cloud.storage==1.32.0", # for gcp backups
           "gsutil==4.41", # for gcp backups
           "matplotlib==3.1.1", # used for data exploration
           "pandas==1.3.5", # for dataframes manipulation
           "pyarrow==6.0.1", # to load parquet files
           "unidecode==1.1.1", # to clean accents in cleaner
           "xlrd==1.2.0", # to load excel files
           "google-cloud-secret-manager==2.8.0", # Manage secret
           "db-dtypes==0.3.1", # Load joblib with sql bigquery
           "docker==5.0.3", # Docker api
           "pytest==6.1.2",
           "pytest-schema==0.1.1"
                ],
    include_package_data=True,
    description='Test Data Engineer',
    author='Baruch AMOUSSOU-DJANGBAN',
    license='MIT'
)
