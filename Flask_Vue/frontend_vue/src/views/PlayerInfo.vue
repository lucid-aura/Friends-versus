<template>
    <div class="custom-home">
        <div>
            <p>아래 아이디나와야함</p>
        </div>
        <table>
            <thead>
                <h3 colspan="3"> 플레이어 정보</h3>
            </thead>
            <tbody>
                <tr>
                    <td rowspan = "2">
                        <p>{{ player_info['profileIconId'] }}</p>
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
            player_datas: [],
        }
    },
    method:{
        test(){
            alert("test");
        },

    },
    mounted() {
        console.log("mounted");
    },
    created() {
        console.log("created");
    },

}
</script>
