def fn_copy( base ):
     return base

def fn_upper_all( base ):
     return base.upper()

def fn_lower_all( base ):
     return base.lower()

def fn_upper_first( base ):
     return base[0].upper() + base[1 : len( base )].lower()
