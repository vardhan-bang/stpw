import statement_functions as stf

def ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.ari_statement()}
    return 0;
}}
'''

def if_ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.if_statement()} {{
        {stf.ari_statement()}
    }}
    return 0;
}}
'''

def for_ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.for_statement('i')} {{
        {stf.ari_statement()}
    }}
    return 0;
}}
'''

def if_if_ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.if_statement()} {{
        {stf.if_statement()} {{
            {stf.ari_statement()}
        }}
    }}      
    return 0;
}}
'''

def if_for_ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.if_statement()} {{
        {stf.for_statement('i')} {{
            {stf.ari_statement()}
        }}
    }}        
    return 0;
}}
'''

def for_if_ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.for_statement('i')} {{
        {stf.if_statement()} {{
            {stf.ari_statement()}
        }}
    }}        
    return 0;
}}
'''

def for_for_ari_snippet():
    return f'''int main() {{
    {stf.init_statement()}
    {stf.for_statement('i')} {{
        {stf.for_statement('j')} {{
            {stf.init_statement()}
        }}
    }}
}}
'''

