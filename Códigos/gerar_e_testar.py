"""Base inteiramente SINTÉTICA de componentes analíticos de intangíveis.
Reprodução: python gerar_e_testar.py   (numpy necessário)
TOTVS: totais publicados; todas as linhas individuais são fictícias.
"""
import csv, json, zipfile, random
from pathlib import Path
from datetime import date,timedelta
import numpy as np
ROOT=Path(__file__).resolve().parent
SEED=20251021
RNG=np.random.default_rng(SEED)
N=500_000
# valores públicos, R$ mil. Nota 15 pág. 51 das Notas Explicativas 2025
CLASSES=[
('Software',979674,689819,155000,4,20,13.30),
('Marcas e patentes',153711,106917,35000,2,25,8.57),
('Carteira de clientes',736854,525865,120000,2,20,12.42),
('Ativos de desenvolvimento',223664,66272,140000,2,7,26.76),
('Direito de uso de licenças',20834,3906,15000,4,4,25.02),
('Outros',81337,66181,35000,2,5,20.09)]
GOODWILL=[('UGC Gestão',1341256),('UGC RD',1825883)]
# ponto fixo em centavos de R$ mil = R$ 10; evita erros de ponto flutuante no controle
# armazenamos cada lançamento em reais e centavos (R$), saldos da fonte (mil R$) * 1000
# em dados reais do PDF, os saldos são arredondados ao milhar.

def apport(total,weights):
    x=weights/weights.sum()*total
    a=np.floor(x).astype(np.int64)
    residual=int(total-int(a.sum()))
    if residual: a[np.argsort(x-a)[-residual:]]+=1
    return a

def allocate_amort(cost,target,ratio):
    # Redistribuir de forma sintética, com idade estimada, respeitando amort <= custo
    lo,hi=0.,10000.
    for _ in range(55):
        mid=(lo+hi)/2
        amt=np.minimum(cost,np.floor(cost*ratio*mid).astype(np.int64))
        if int(amt.sum())<target:lo=mid
        else:hi=mid
    a=np.minimum(cost,np.floor(cost*ratio*hi).astype(np.int64))
    delta=int(target-int(a.sum()))
    if delta>0:
        ix=np.flatnonzero(a<cost)
        a[ix[:delta]]+=1
    elif delta<0:
        ix=np.flatnonzero(a>0)
        a[ix[:abs(delta)]]-=1
    assert int(a.sum())==target and np.all(a>=0) and np.all(a<=cost)
    return a

rows=[]
errors=[]
summary=[]
for cls,cost_mil,amort_mil,n,miny,maxy,rate in CLASSES:
    gross=int(cost_mil*100000)  # convert R$ mil into centavos de R$
    accum=int(amort_mil*100000)
    w=RNG.gamma(2.2,1,size=n)
    cost=apport(gross,w)
    useful=RNG.integers(miny*12,maxy*12+1,size=n)
    # data de disponibilidade é fictícia; mais antiga para classes com maior amortização
    months=RNG.integers(0,maxy*12+20,size=n)
    ratio=np.minimum(1,months/useful)
    amort=allocate_amort(cost,accum,ratio+0.005)
    r=[(cls,int(c),int(a),int(u),int(m)) for c,a,u,m in zip(cost,amort,useful,months)]
    rows.extend(r)
    summary.append({'classe':cls,'quantidade':n,'custo_rs':cost_mil*1000,'amortizacao_acumulada_rs':-amort_mil*1000,'saldo_liquido_rs':(cost_mil-amort_mil)*1000})
assert len(rows)==N
raw=ROOT/'intangiveis_sinteticos_500000.csv'
with raw.open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f,delimiter=';')
    writer.writerow(['id_componente','classe','id_projeto_sintetico','id_ugc_sintetica','data_disponivel','vida_util_meses','custo_centavos','amortizacao_acumulada_centavos','saldo_liquido_centavos','valor_original_centavos','indicador_erro','natureza_dado'])
    for i,(cls,c,a,u,m) in enumerate(rows,1):
        d=date(2025,12,31)-timedelta(days=int(m*365.25/12))
        # Cada linha é um componente de custo individual distinto, não um 'ativo' completo.
        writer.writerow([f'INT{i:07d}',cls,f'PROJ{i//25:06d}',f'UGC-S{(i%4)+1}',d.isoformat(),u,c,a,c-a,c,'NAO','SINTETICO'])
# Erros injetados em arquivo CÓPIA com 100 erros conhecidos, sem comprometer conciliação do livro-base
indices=sorted(RNG.choice(N,size=100,replace=False).tolist())
# Criar amostra de 100 erros para testar regras sem regravar base 500 mil
with (ROOT/'excecoes_injetadas.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter=';');w.writerow(['id_componente','tipo_erro','valor_original','valor_adulterado','natureza'])
    for i in indices:
        cls,c,a,u,m=rows[i]
        typ='AMORTIZACAO_SUPERIOR_AO_CUSTO' if i%2==0 else 'VIDA_UTIL_ZERO'
        w.writerow([f'INT{i+1:07d}',typ,a if i%2==0 else u,c+100 if i%2==0 else 0,'SINTETICO'])
with (ROOT/'goodwill_por_ugc.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter=';');w.writerow(['ugc','valor_rs','natureza_dado','criterio'])
    for name,amount in GOODWILL:w.writerow([name,amount*1000,'SALDO_PUBLICADO','Nota 15.1 da DFP 2025; não são linhas simuladas'])
actual_gross=sum(x['custo_rs'] for x in summary);actual_accum=sum(x['amortizacao_acumulada_rs'] for x in summary)
assert (actual_gross+actual_accum+sum(x[1]*1000 for x in GOODWILL))==3904253000
output={'marcacao':'TODOS OS 500000 COMPONENTES SAO SINTETICOS; SALDOS DE CONTROLE SAO PUBLICOS','ano':2025,'moeda':'BRL','unidade_base':'centavos de real, valores numéricos inteiros','seed':SEED,'registros':N,'por_classe':summary,'goodwill_publicado_rs':sum(x[1]*1000 for x in GOODWILL),'custo_sintetico_total_rs':actual_gross,'amortizacao_sintetica_total_rs':actual_accum,'liquido_sintetico_sem_goodwill_rs':actual_gross+actual_accum,'intangivel_com_goodwill_rs':actual_gross+actual_accum+sum(x[1]*1000 for x in GOODWILL),'saldo_publicado_intangivel_rs':3904253000,'diferenca_rs':0,'excecoes_injetadas_separadamente':len(indices),'observacao':'O ajuste dos saldos sintéticos aos totais publicados é por construção matemática, não confirma registros reais. Amortização distribuída sinteticamente, não se confunde com teste independente de vida útil ou encargos.'}
(ROOT/'resultado_validacao.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf8')
with zipfile.ZipFile(ROOT/'intangiveis_sinteticos_500000.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:z.write(raw,raw.name)
print('OK',N,'base',raw.stat().st_size,'zip', (ROOT/'intangiveis_sinteticos_500000.zip').stat().st_size,'totais',output['intangivel_com_goodwill_rs'])
