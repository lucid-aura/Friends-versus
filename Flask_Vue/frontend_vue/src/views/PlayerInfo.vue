<template>
    <div class="custom-home">
        <table>
            <thead>
                <h3 colspan="3"> {{ player_info['name'] }} </h3>
            </thead>
            <tbody>
                <tr>
                    <td rowspan = "2">
                        <img :src=this.url   id="player_icon" style="width: 50%; height: 50%"/>
                        
                    </td>
                    <td>
                        <p>닉네임 {{ player_info['name'] }}</p>
                    </td>
                    <td>
                        <p>Level.{{ player_info['summonerLevel'] }}</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>최근 경기 시간 : {{ player_info['revisionDate'] }} </p>
                    </td>
                </tr>
            </tbody>
        </table>
        <table>
            <h3> 최근 10경기 </h3>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        id: String,
        player_info: Object
    },
    data() { // DB로 받아오는 과정이 필요함. 스크립트 내 저장된 데이터를 쓰는 것이 아니라...
        return {
            url: "",
        }
    },
    method:{
        geturl(){
            return this.url
        },
        resolve_img_url(){
            
            let path = "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/";
            //path += picture_src;
            //path += ".png";
            path = "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/588.png";
            return path
        },
        test(){
            var path = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/';
            path += this.player_info['profileIconId'];
            path += '.png'
            document.getElementById("player_icon").src =path;
            return path
        },

    },
    mounted() {
        var path = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/';
        path += this.player_info['profileIconId'];
        path += '.png'
        this.url = path
        document.getElementById("player_icon").src =path;
        console.log("mounted");
    },
    created() {
        
        //icon.setAttribute("src", "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/588.png");
        //icon.src = "http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/588.png";
    
        console.log("created");
    },

}
</script>
