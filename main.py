import re

def check_vulnerabilities(contract_code):
    if "call.value" in contract_code or "send" in contract_code:
        print("⚠️ Possible Reentrancy Vulnerability Detected!")
    if "uint" in contract_code and "unchecked" not in contract_code:
        print("⚠️ Potential Integer Overflow Risk!")
    # Add more checks here...

# Example Solidity Code
solidity_code = """
pragma solidity ^0.8.0;
contract Test {
    function withdraw() public {
        msg.sender.call.value(1 ether)();
    }
}
"""
check_vulnerabilities(solidity_code)
