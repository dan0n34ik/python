import json

with open('firms.txt', encoding='utf-8') as mf:
    pr_summ = 0
    ub = 0
    my_list = [{}, {}]
    for i in mf.readlines():
        pribl_or_ub = int(i.split()[2]) - int(i.split()[3])
        my_list[0].update({i.split()[0]: abs(pribl_or_ub)})
        if pribl_or_ub > 0:
            pr_summ += pribl_or_ub
        else:
            ub += 1
    mf.seek(0)
    my_list[1].update({'average_profit': pr_summ / (len(mf.readlines()) - ub)})
with open('my_json.json', 'w', encoding='utf-8') as json_f:
    json.dump(f'{my_list}\n', json_f, ensure_ascii=False)
