def get_reli_id(reli_name):
    return {'hindu':1, 'budd':2, 'christian':3, 'catholic':4, 'islam':5, 'juda':6, 'sikh':7, 'none':8}.get(reli_name, 8)

def get_vege_id(vege_name):
    return {'vegan':1, 'lacto':2, 'ovo':3, 'lactoovo':4, 'pesco':5, 'flo':6, 'flexi':7}.get(vege_name, 8)