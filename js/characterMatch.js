exports.isCharacterMatch = function(string1, string2) {
    let sortStr1 = removeSpace(string1.toLowerCase().split('').sort())
    let sortStr2 = removeSpace(string2.toLowerCase().split('').sort())
    if(sortStr1.length !== sortStr2.length) return false;
    for(let i = 0; i < sortStr1.length; i++){
        if(sortStr1[i] !== sortStr2[i]) return false;
    }
    return true;
};

function removeSpace(arr){
    return arr.filter(word => word !== " ")
}
