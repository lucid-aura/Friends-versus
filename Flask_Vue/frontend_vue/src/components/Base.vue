<template>
    <div>
        <router-view :login_id=this.login_id />
    </div>
</template>

<script>
    export default {
        name: 'Base',
    data() {
        return {
            login_id: ''
        }
    },
}
</script>