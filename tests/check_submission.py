"""Validate the schema keywords used by the frozen course contracts."""
from pathlib import Path
import json, subprocess, sys
r=Path(__file__).resolve().parents[1]
a=r/'agents/innovation_disruption'
def check(value,schema,path='$'):
    types={'object':dict,'array':list,'string':str}
    if 'type' in schema: assert isinstance(value,types[schema['type']]), path+' wrong type'
    if isinstance(value,dict):
        assert set(schema.get('required',[])) <= set(value),path+' missing required fields'
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False: assert set(value)<=set(props),path+' extra fields'
        for k,v in value.items():
            if k in props: check(v,props[k],path+'.'+k)
    if isinstance(value,list) and 'items' in schema:
        for i,v in enumerate(value): check(v,schema['items'],path+f'[{i}]')
subprocess.run([sys.executable,str(r/'tools/check_frozen_core.py')],check=True)
for kind,folder in [('input','cases'),('output','responses')]:
    schema=json.loads((r/'core'/f'{kind}_schema.json').read_text())
    for p in sorted((a/folder).glob('*.json')):
        check(json.loads(p.read_text()),schema)
        if kind=='output': subprocess.run([sys.executable,str(r/'tools/validate_response.py'),str(p)],check=True)
        print('Contract PASS:',p.relative_to(r),flush=True)
x=[json.loads((a/'responses'/f'{n}_response.json').read_text()) for n in ['primary','contrast_1','contrast_2']]
assert len({v['general_et_finding'] for v in x})==1
for label,v in zip(['Low','High','Insufficient information'],x):
    assert 'Business-Model Disruption Judgment: '+label in v['organization_specific_finding']
assert len(x[2]['abstention_or_more_information_needed'])>=3
# Ensure proposed deployments are not represented as measured completed innovations.
assert 'not yet an implemented innovation' in x[0]['application_finding']
assert 'not proof of paying adoption' in x[1]['application_finding']
# Check the checker rejects an unexpected top-level field and a mistyped evidence item.
for mutation in ['extra','evidence']:
    bad=json.loads(json.dumps(x[0]))
    if mutation=='extra': bad['unexpected']=True
    else: bad['evidence'][0]['claim']=42
    try: check(bad,json.loads((r/'core/output_schema.json').read_text()))
    except AssertionError: pass
    else: raise AssertionError('Validator accepted malformed output')
print('Stable/general and changed/contextual findings PASS; abstention PASS; malformed-output rejection PASS.')
print('Checks validate saved artifact structure and consistency, not forecasts or independent LLM reliability.')
