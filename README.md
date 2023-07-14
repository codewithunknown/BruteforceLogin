# Teaching Platform Vulnerability and User Experience Feedback

This repository contains details of a vulnerability discovered on the Teaching platform, as well as user experience feedback. The purpose of this repository is to provide comprehensive information about the vulnerability and its potential impact.

## Vulnerability Details

### Description
The login route on the Teaching platform (pupilfirst.com) has a potential vulnerability that allows for brute-force attacks. By repeatedly making requests to the `/get_magic_link` route, an attacker could trigger multiple email sending requests, resulting in additional costs for the email service.

### Mitigation
To mitigate this vulnerability, it is recommended to implement Google reCAPTCHA to add an extra layer of security and prevent automated brute-force attacks.

