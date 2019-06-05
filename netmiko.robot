*** Settings ***
Library    OperatingSystem
Library    NetmikoOperator.py

** Variables **
${IP}   18.215.36.232
${user}     ntc
${pass}     ntc123
${device}       cisco_ios     
${hostname}     csr1
${ifname}       GigabitEthernet1
${command}      show ip interface brief

*** Test Cases ***
Login to router
    OPEN SESSION    ${IP}    ${user}    ${pass}    ${device}    ${hostname}

Check if state : Initial check
    ${return}=    CHECK IF STATE    ${ifname}    ${hostname}    ${command}
    Should Be True    ${return}