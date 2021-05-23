pragma solidity >= 0.5.0 < 0.7.0;

contract MyName {
    string public myName;

    constructor() public {
        myName = "Solidity";
    }

    function setMyName(string memory _myName) public {
        myName = _myName;
    }

    function sayMyName() view public returns (string memory) {
        return myName;
    }
}