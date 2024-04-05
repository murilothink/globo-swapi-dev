import logging
import os
import warnings

warnings.filterwarnings("ignore")
APP_ENV = os.getenv("app_env", "prd")

# OBTER REQUEST API FILMS
SWAPI_DEV_FILMS = 'https://swapi.dev/api/films/'
VAULT_LOGIN_URI = '/v1/auth/userpass/login/usr-extrato-hml'
VAULT_SECRET_URI = '/v1/app/data/robo/hml/extrato/extrato-letters'

# ENVIO DE E-MAIL
MSGRAPH_BASE_URL = 'https://graph.microsoft.com'
MSGRAPH_SEND_MAIL_URI = '/v1.0/users/5ab0f8d3-a20d-4b23-a925-7d58d0604441/sendMail'
MSGRAPH_SEND_URL = f'{MSGRAPH_BASE_URL}{MSGRAPH_SEND_MAIL_URI}'
MSGRAPH_SCOPE_URI = '/.default'
MSGRAPH_SCOPE_URL = f'{MSGRAPH_BASE_URL}{MSGRAPH_SCOPE_URI}'

# OBTER TOKEN GRAPH
MSLOGIN_BASE_URL = 'https://login.microsoftonline.com/{tenant_id}'
MSLOGIN_URI = '/oauth2/v2.0/token'
MSLOGIN_URL = f'{MSLOGIN_BASE_URL}{MSLOGIN_URI}'

if APP_ENV == "local":
    '''
    PATH_ANEXOS = 'C:\\carta\\arquivos'
    PATH_EXCEL = 'C:\\carta\\excel'
    PATH_LOG = 'C:\\carta\\log\\log_envio.csv'
    '''

    '''
    PATH_ANEXOS = '/home/gisela.araujo/Documentos/automatizacao'
    PATH_EXCEL = '/home/gisela.araujo/Documentos/automatizacao'
    PATH_LOG = '/home/gisela.araujo/Documentos/automatizacao/log_envio.csv'    
    '''

    PATH_ANEXOS = 'P:\\Documents\\automatizacao'
    PATH_EXCEL = 'P:\\Documents\\automatizacao'
    PATH_LOG = 'P:\\Documents\\automatizacao\\log_envio.csv'

    '''
    PATH_ANEXOS = '/home/T0905GSC/carta/data'
    PATH_EXCEL = '/home/T0905GSC/carta/data'
    PATH_LOG = '/home/T0905GSC/carta/data/log_envio.csv'
    '''
    BACKOFFICE_MAIL = ['t0905gsc@prestadorcbmp.com.br', 't0611mth@prestadorcbmp.com.br']

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

logging.info(f'Send email URL: {MSGRAPH_SEND_URL}')
logging.info(f'MS Graph scope: {MSGRAPH_SCOPE_URL}')
logging.info(f'MS Graph auth URL: {MSLOGIN_URL}')

