import requests
import json

cep = str(input("Informe um CEP: "))

consulta = requests.get('https://viacep.com.br/ws/{0}/json/'.format(cep))

consulta = json.loads(consulta.content)

print("CEP: ", consulta["cep"])
print("Logradouro: ", consulta["logradouro"])
print("Complemento: ", consulta["complemento"])
print("Bairro: ", consulta["bairro"])
# print("Localidade: ",consulta["localidade"])
print("UF: ", consulta["uf"])
# print("IBGE: ",consulta["ibge"])
# print("GIA: ",consulta["gia"]);
print("DDD: ", consulta["ddd"])
# print("SIAFI: ",consulta["siafi"])
