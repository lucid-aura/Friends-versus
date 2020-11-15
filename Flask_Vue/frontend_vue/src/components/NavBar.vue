<template>
    <header class="masthead mb-auto site-header">
        <div class="inner">
            <nav class="nav nav-masthead justify-content-center">
                <router-link to="/" class="nav-link" exact>
                    Home
                </router-link>
                <router-link to="/friendlist" class="nav-link" exact>
                    Friend list
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