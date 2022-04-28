*** Settings ***
Library    FaceLibrary

*** Variables ***
${TESTDATA}    ${CURDIR}/testdata

*** Test Cases ***
Image Should Contain Face
    Should Contain A Face    ${TESTDATA}/faces.png

Image Should Not Contain A Face
    Should Not Contain A Face    ${TESTDATA}/no_faces.jpg

Check Exceptions
    Run Keyword And Expect Error    
    ...    Image should contain a face. But no face was detected    
    ...    Should Contain A Face    ${TESTDATA}/no_faces.jpg

    Run Keyword And Expect Error
    ...    Image should NOT contain a face. But it contains a face    
    ...    Should Not Contain A Face    ${TESTDATA}/faces.png



