function compute ( arr ){
    let prefix = arr[0];
    let prevPrefix = prefix;
    let prevPrefixCount = 1;
    
    let inlineItemCount = 1;
    for( let i = 1 ; i < arr.length  ; i++ ){
        const str = arr[i];
        let prefixCount = 0;
        for( let j = 0 ; j < str.length ; j++ ){
            if( str[j] == prefix[j] ){
                prefixCount++;
            }
            else break;
        }
        
        if( prefixCount > 0 ) {
            inlineItemCount++;
            if( prefixCount < prefix.length ){
                prefix = prefix.slice(0 , prefixCount);
            }
        }
        
        else {
            if( inlineItemCount >= prevPrefixCount ){
                prevPrefixCount = inlineItemCount;
                prevPrefix = prefix;
                inlineItemCount = 0;
            }
            
            prefix = str;
        }
    }
    
    return prevPrefix;
}

const arr = ['asd1','asd12','fdfdf','dddsd','789kley','8789kl','789kuu','asd'];

console.log(compute(arr));