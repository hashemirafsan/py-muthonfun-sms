from muthofun_sms import Muthofun

r = Muthofun({
    'username': 'hashemirafsa',
    'password': '01625903501RrR'
}).message('Hellow Rafsan').to('01818400400').send([
    {
        'sms': 'Rafsan',
        'to': [
            '01717408297'
        ]
    },
    {
        'sms': 'Rafsan',
        'to': '01717408297'
    }
])

print(r)