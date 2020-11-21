<template>
    <div class="custom-home">
        <table>
            <thead>
                <h3 colspan="3"> 플레이어 정보</h3>
            </thead>
            <tbody>
                <tr>
                    <td rowspan = "2">
                        <p>{{ player_data[0].profileIconId }}</p>
                    </td>
                    <td>
                        <p>닉네임 {{ id }}</p>
                    </td>
                    <td>
                        <p>Level.{{ player_data[0].summonerLevel }}</p>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <p>최근 경기 시간 : {{ player_data[0].revisionDate }} </p>
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
        id: String
    },
    name: 'championList',
    data() { // DB로 받아오는 과정이 필요함. 스크립트 내 저장된 데이터를 쓰는 것이 아니라...
        return {
            player_data: [
                {
                    "id": "DSysYVtTtCikX_KPElUN1FgzRcDzBwBuYOnYZ-rImUlAgg",
                    "accountId": "ocszCxil4hSsLfkm2jds_6p97_UDmFGe_95Fu37j9y7K",
                    "puuid": "e0wX5c8UW2WFWhC36nKTi1c3NcALQoztvD9qjqgZNNoG97KHNth-acac1-a-BIIhtFN1U3fNH7KZ_w",
                    "name": "휘 랑",
                    "profileIconId": 4626,
                    "revisionDate": 1605589023000,
                    "summonerLevel": 358
                }
            ],
        }
    },
}
</script>
