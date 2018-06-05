from setuptools import setup

exec (open('dash_devextreme/version.py').read())

setup(
    name='dash_devextreme',
    version=__version__,
    author='pikhovkin',
    packages=['dash_devextreme'],
    include_package_data=True,
    license='MIT',
    description='Wrapper of DevExtreme components for Plotly Dash',
    install_requires=[]
)
