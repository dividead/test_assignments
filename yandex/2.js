function reversePrint(linkedList, a = []) {
    a.unshift(linkedList.value)
    linkedList.next ? reversePrint(linkedList.next, a) : console.log(a)
}

var someList = {
    value: 1,
    next: {
        value: 2,
        next: {
            value: 3,
            next: {
                value: 4,
                next: null
            }
        }
    }
};

reversePrint(someList);


