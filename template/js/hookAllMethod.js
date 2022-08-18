Java.perform(function(){
    //hook 类所有方法
    var str_cls_name = "com.example.test_tracker.Test"; //类名

    //获取类的所有方法
    var cls = Java.use(str_cls_name);
    var mhd_array = cls.class.getDeclaredMethods();

    //hook 类所有方法 （所有重载方法也要hook)
    for (var i = 0; i < mhd_array.length; i++)
    {
        var mhd_cur = mhd_array[i]; //当前方法
        var str_mhd_name = mhd_cur.getName(); //当前方法名
        //console.log(str_mhd_name);

        //当前方法重载方法的个数
        var n_overload_cnt = cls[str_mhd_name].overloads.length;
        //console.log(n_overload_cnt);

        for (var index = 0; index < n_overload_cnt; index++)
        {
            cls[str_mhd_name].overloads[index].implementation = function ()
            {
                console.log("start: " + str_mhd_name);
                //参数个数
                var n_arg_cnt = arguments.length;

                for (var idx_arg = 0; idx_arg < n_arg_cnt; n_arg_cnt++)
                {
                    console.log(arguments[idx_arg]);
                }

                console.log("end: " + str_mhd_name + '--' + n_arg_cnt);
                return this[str_mhd_name].apply(this, arguments);
            }
        }
    }
});


Java.perform(function(){
    var cls = Java.use("类路径");
    var methods = cls.class.getDeclaredMethods();
    for(var j = 0; j < methods.length; j++){
        var methodName = methods[j].getName();
        console.log(methodName);

        for(var k = 0; k < cls[methodName].overloads.length; k++){

            cls[methodName].overloads[k].implementation = function(){
                for(var i = 0; i < arguments.length; i++){
                    console.log(arguments[i]);
                }
                return this[methodName].apply(this, arguments);
            }
        }
    }
})
