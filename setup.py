from setuptools import setup, find_packages

setup(
    name='pygeon',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',  # Para enviar mensagens via Telegram
    ],
    description='Um pacote para enviar mensagens via Telegram, email e outros canais.',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/seu_usuario/pygeon',
)
