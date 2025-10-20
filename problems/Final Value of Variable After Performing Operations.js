/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let X = 0;
    for (const operation of operations) {
        eval(operation);
    }
    return X;
};