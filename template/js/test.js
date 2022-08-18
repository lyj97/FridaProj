
console.log("[*]  Java Starting script");
Java.perform(function() {
    var dexclassLoader= Java.use('ese.xposedtest.MainActivity');
    //外部类 的OutClass方法  修改返回值
    dexclassLoader.OutClass.implementation = function () {
        var ret = this.OutClass();
        console.log('Done:' + JSON.stringify(ret));
        return "Frida "+ret;
    }

    //内部类
    var dexclassLoader1= Java.use('ese.xposedtest.MainActivity$inClasse');
    //打印参数 的formInclass方法 参数随意修改了
    dexclassLoader1.formInclass.implementation = function()
    {
        var arg0 = arguments[0];
        var arg1 = arguments[1];
        send("params1: "+arg0+" params2: "+arg1);
        return this.formInclass(1,"Frida");
    }

});
