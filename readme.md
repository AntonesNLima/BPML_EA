#Instruções Básicas:

__*Obs:*__ Os arquivos __interpolate.py__ e __padronizacao.py__ são os scripts que renderam melhor acurácia. Caso queira tentar reproduzir o resultado, execute os scripts nesta ordem, usando o .xlsx original. 

- __interpolate.py__ é o responsável pela imputação dos dados, através do método de interpolação.

- __padronizacao.py__ é responsável pela normalaização dos dados, usando o método de padronização ou Z-Score.
- __reescala.py__ é responsável pela normalização por reescala.

- __EDA.py__ é responsável pela geração dos dados de análise exploratória. Também gera alguns gráficos, incluindo o mapa de correlação.

- O arquivo __linearReg.py__ é um script para preenchimento de dados faltantes usando regressão linear. Mas a acurácia foi inferior à da interpolação. 

- __outliersRm.py__ remove possíveis dados discrepantes, mas isso causa uma redução abrupta de accuracy.Por este motivo não foi incluso nos testes.

- __checkDuplicated.py__ procura por registros duplicados. Não foi encontrado nenhum registro duplicado.

