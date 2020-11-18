<template>
    <header class="masthead mb-auto site-header">
        <div class="inner">
            <nav class="nav nav-masthead justify-content-center">
                <router-link to="/" class="nav-link" exact>
                    Home
                </router-link>
                <router-link to="/friendlist" exact>
                    <button id= "login" class="nav-link" :disabled="true">
                        Friend list
                    </button>
                </router-link>
                <router-link to="/itemlist" class="nav-link" exact>
                    Items
                </router-link>
                <router-link to="/championlist" class="nav-link" exact>
                    Champions
                </router-link>
            </nav>
        </div>
    </header>
</template>

<script>
export default {
    name: 'NavBar',
    data() {
        return{
            check_login: 'false',
            user_name: ''
        }
    },
    able(user) {
        var btn = document.getElementById('login');
        btn.disabled= false
        this.user_name = user
        //console.log(this.user_name)
        //onsole.log(user)
    },
    methods: {
        prevent: function() {
            alert(this.check_login)
            console.log(this.check_login)
            this.check_login = false
        }
    }
}
</script>