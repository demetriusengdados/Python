#Função para obter data futura após N dias uteis 

def getFutureWorkDate (p_StartDate, p_SlaDays):
    """
    Def:
        Obtem a data futura após decorrer N dias uteis
    Args:
        p_StartDate - Data Inicial em formato YYYY-MM-DD HH:MI:SS
        p_SlayDays  - SLA em dias

    Returns:
        A data futura após N dias uteis informado pela p_SlayDays

    Call Example:
        getFutureWorkDate ("2023-06-01 08:00:00", 5)
    """

from business_duration import businessduration
import pandas as pd
import holidays
import datetime.pytz
from pyspark.sql.functions import length,trim

#formatando a data 
start_date = datetime.datetime.strptime(p_StartDate, "%Y-%M-%D %H:%M:%S")

#Lista com os fins de semana (sabado/domingo)
BR_weekend_list = [5,6]

#lista com os feriados nacionais deste ano e proximo
BR_holiday_list = holidays.Brazil(years = [start_date.year, start_date.year+1])
wtoWorkDays = 0
wcurrentDate = start_date
one_day = datetime.timedelta(days=1)

# A partir da data atual vou adicionando 1 dia, verificando se é feriado ou fim de semana
#Só termino quando a "data futura", após N dias uteis informado pelo SLADAYS

while p_SLADays >= wtoWorkDays:
    if wcurrentDate.weekday() not in BR_weekend_list and wcurrentDate.strftime("%y-%m-%d") not in BR_holiday_list:
        wtoWorkDays += 1

    #Adiciono mais um dia na data quando o limite é atingido 
    if p_SLADays >= wtoWorkDays:
        wcurrentDate += one_day

    #retorno a data no formato abaixo:
    return datetime.datetime.strftime(wcurrentDate, "%y-%m-%d %H:%M:%S")
