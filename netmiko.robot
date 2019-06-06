*** Settings ***
Library    OperatingSystem
Library    utils/NetmikoOperator.py

** Variables **
${ip}   18.215.36.232
${user}     ntc
${pass}     ntc123
${device}       cisco_ios     
${hostname}     csr1
${command}      show ip interface brief

*** Test Cases ***
Login to device
    OPEN SESSION    ${ip}    ${user}    ${pass}    ${device}    ${hostname}

Check if state : Initial check
    ${return}=    show ip int br      ${hostname}    ${command}
    Should Be True    ${return}

Clean up Connection with device
    CLOSE SESSION    ${hostname}