from ir import IR


ir = IR(26)

power = True

while power:
    key = ir.get_ir_key()
    
    if key is not None:
        print(key)
        
        if key == 'Power':
            power = False
