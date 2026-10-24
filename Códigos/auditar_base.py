"""Testes independentes simples: população e 100 erros sintéticos conhecidos."""
import csv, json
from collections import defaultdict,Counter
from pathlib import Path
P=Path(__file__).resolve().parent
source=P/'intangiveis_sinteticos_500000.csv'
expected=json.loads((P/'resultado_validacao.json').read_text())
by_class=defaultdict(lambda:[0,0,0]);ids=set();bad=[];count=0
with source.open(encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f,delimiter=';'):
  count+=1;id=r['id_componente'];cls=r['classe']
  c=int(r['custo_centavos']);a=int(r['amortizacao_acumulada_centavos']);net=int(r['saldo_liquido_centavos'])
  if id in ids:bad.append((id,'ID_DUPLICADO'))
  ids.add(id)
  if not 0<=a<=c or net!=c-a:bad.append((id,'SALDO_INCONSISTENTE'))
  if int(r['vida_util_meses'])<=0:bad.append((id,'VIDA_UTIL_INVALIDA'))
  b=by_class[cls];b[0]+=1;b[1]+=c;b[2]+=a
assert count==500_000
for x in expected['por_classe']:
 n,c,a=by_class[x['classe']]
 assert n==x['quantidade'] and c==x['custo_rs']*100 and a==-x['amortizacao_acumulada_rs']*100
assert not bad
injected=[]
with (P/'excecoes_injetadas.csv').open(encoding='utf8',newline='') as f:
 for x in csv.DictReader(f,delimiter=';'):
  observed='AMORTIZACAO_SUPERIOR_AO_CUSTO' if x['tipo_erro']=='AMORTIZACAO_SUPERIOR_AO_CUSTO' and int(x['valor_adulterado'])>0 else 'VIDA_UTIL_ZERO'
  assert observed==x['tipo_erro']
  injected.append(x['id_componente'])
assert len(injected)==100 and len(set(injected))==100
result={'registros_conferidos':count,'ids_unicos':len(ids),'inconsistencias_base_original':len(bad),'cenarios_de_erro_no_gabarito':len(injected),'observacao':'Exceções são cenários no arquivo externo, não erros encontrados na base original.'}
(P/'resultado_testes.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print(result)
