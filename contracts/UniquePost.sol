pragma solidity >=0.4.22 <0.9.0;

contract UniquePost {
    address private syp = msg.sender; // an address of our own
    address public owner = msg.sender;
    // we need dead time
    uint public last_completed_migration;

    modifier restricted() {
        require(
            msg.sender == syp,
            "This function is restricted to the syp"
        );
        _;
    }

    function setCompleted(uint completed) public restricted {
        last_completed_migration = completed;
    }
}