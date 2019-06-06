*** Settings ***
Library    Collections
Library    utils/test_nso.py

** Variables **
${nso_devicename}       csr1
${command}      show version
${ios_version}      16.06.02
${acl_ip_to_find}       91.118.192.128
${device_type}      ios-xe
*** Test Cases ***



Check Sync NSO against a Live Device: Initial check
    ${return}=    Check Sync   ${nso_devicename}
    Should Be True    ${return}

Verify IOS Version is Correct
    ${return}=    Send Cli Cmd   ${nso_devicename}  ${command} 
    Should Contain    ${return}     ${ios_version} 
Verify IP is in ACL
    @{return}=    Find IP Access List   ${acl_ip_to_find} ${device_type}
    Log List  ${return}
    :FOR  ${acl_iter}  IN  @{return}
    \    ${rule}=  Get From Dictionary  ${acl_iter}  rule
    \    Log  ${rule}
    # \    # Option 2
    # \    Log  ${acl_iter["rule"]}
    # \    Should Contain  ${acl_iter["rule"]}  ${acl_ip_to_find}
    END

