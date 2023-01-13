# Standard imports
import os


ATIEH_INSURANCE_INFO = {
    'login_url': 'https://rasatpa.ir/sso/login?service=https%3A%2F%2Frasatpa.ir%2Fhcp%2Flogin%2Fcas',
    'inquiry_url': 'https://rasatpa.ir/hcp/reception/inquiryInsuredPerson',
    'login_data': {
        'username': str(os.getenv('ATIEH_USERNAME', '')),
        'password': str(os.getenv('ATIEH_PASSWORD', '')),
        'execution': 'e1s1',
        '_eventId': 'submit',
    },
}


DANA_INSURANCE_INFO = {
    'login_url': 'https://totalapp2.dana-insurance.ir/Sepad1/Security',
    'inquiry_url': (
        'https://totalapp2.dana-insurance.ir/Sepad1/Fanavaran/'
        'GetDataBimenameBimeShodeFanByCodeMeliTarikh?tarikhHazine=1401/10/13&CodeMelli={national_code}'
    ),
    'login_data': {
        'NameKarbari': str(os.getenv('DANA_USERNAME', '')),
        'RamzeObor': str(os.getenv('DANA_PASSWORD', '')),
    },
}

IRAN_INSURANCE_INFO = {
    'login_url': (
        'https://darman.iraninsurance.ir/dms-cas/'
        'login?service=http%3A%2F%2Fdarman.iraninsurance.ir%2F%2Fj_spring_cas_security_check'
    ),
    'inquiry_url': 'http://darman.iraninsurance.ir/home-flow?execution=e1s1',
    'login_data': {
        'username': str(os.getenv('IRAN_USERNAME', '')),
        'password': str(os.getenv('IRAN_PASSWORD', '')),
    },
}

MAD_INSURANCE_INFO = {
    'login_url': 'https://mccp.iraneit.com/core/connect/token',
    'inquiry_url': (
        "https://mccp.iraneit.com/odata/MCClaimProc/preAuthEnabledPolicy/getInsuredPersonPolicyInfo"
        "(corpId={insurance_id},nationalCodeOrId='{national_code}',type='nationalcode')?$top=1"
    ),
    'login_data': {
        'scope': 'openid profile user_info',
        'grant_type': 'password',
        'username': str(os.getenv('MAD_USERNAME', '')),
        'password': str(os.getenv('MAD_PASSWORD', '')),
        'client_id': 'MCClaimProc-ResOwner',
        'client_secret': 'secret',
    },
}

SOS_INSURANCE_INFO = {
    'login_url': 'https://carewrapper.iranassistance.com/Auth/Authentication/LoginUser',
    'inquiry_url': 'https://carewrapper.iranassistance.com/api/CareCenter/GetContractList',
}

TAMIN_INSURANCE_INFO = {
    'inquiry_url': 'https://medical.tamin.ir/api/medical-support/v2.0/{national_code}',
}
