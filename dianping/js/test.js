
console.log("[*]  Java Starting script");
Java.perform(function() {

    var cla_act_shopinfo = Java.use('com.dianping.shopshell.ShopInfoActivity');
//    cla_act_shopinfo.onCreate.implementation = function (param) {
//        console.log('onCreate:' + JSON.stringify(arguments[0]));
//        console.log('onCreate:' + JSON.stringify(param));
//        return this.onCreate(param);
//    }

    var cls = cla_act_shopinfo;
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

//                for (var idx_arg = 0; idx_arg < n_arg_cnt; n_arg_cnt++)
//                {
//                    console.log(arguments[idx_arg]);
//                }

                console.log("end: " + str_mhd_name + '--' + n_arg_cnt);
                return this[str_mhd_name].apply(this, arguments);
            }
        }
    }

});
