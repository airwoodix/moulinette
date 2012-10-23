# -*- coding: utf-8 -*-

import yaml

def tools_init(args, connections): 
    yldap = connections['ldap']
    
    with open('ldap_scheme.yml') as f: 
        ldap_map = yaml.load(f)

    for rdn, attr_dict in ldap_map['parents'].items():
        yldap.add(rdn, attr_dict)

    for rdn, attr_dict in ldap_map['childs'].items():
        yldap.add(rdn, attr_dict)