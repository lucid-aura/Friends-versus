<template style="background-color:#000000">
    <div class="custom-home">
        <div>
            <table class="champion-info">
                <thead>
                    <tr>
                        <td>{{ info_list[0] }}</td>
                        <td>{{ info_list[1] }}</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td> <img :src=this.champion_square /> </td>
                        <td> {{ info_list[3] }} </td>
                        <td> {{ info_list[4] }} </td>
                    </tr>
                    <tr>
                        <td colspan = "3">
                            챔피언 스킨
                        </td>
                    </tr>
                    <tr>
                        <td colspan = "3">
                            챔피언 스킨
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div>
            <div class="stat-div">
                <table class="stat-table">
                    <thead>
                        <tr>
                        <th colspan = "4" scope="cols">챔피언 스탯 정보</th>
                        </tr>
                        <tr>
                        <th scope="row"></th>
                            <td>1레벨</td>
                            <td>레벨업시</td>
                            <td>18레벨</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th scope="row">체력</th>
                            <td>{{ stat_list['hp'] }}</td>
                            <td>{{ stat_list['hpperlevel'] }}</td>
                            <td>{{ stat_list['hp'] + stat_list['hpperlevel'] * 17  }}</td>
                        </tr>
                        <tr>
                        <th scope="row">체력 재생</th>
                            <td>{{ stat_list['hpregen'] }}</td>
                            <td>{{ stat_list['hpregenperlevel'] }}</td>
                            <td>{{ stat_list['hpregen'] + stat_list['hpregenperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">마나</th>
                            <td>{{ stat_list['mp'] }}</td>
                            <td>{{ stat_list['mpperlevel'] }}</td>
                            <td>{{ stat_list['mp'] + stat_list['mpperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">마나 재생</th>
                            <td>{{ stat_list['mpregen'] }}</td>
                            <td>{{ stat_list['mpregenperlevel'] }}</td>
                            <td>{{ stat_list['mpregen'] + stat_list['mpregenperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">공격력</th>
                            <td>{{ stat_list['attackdamage'] }}</td>
                            <td>{{ stat_list['attackdamageperlevel'] }}</td>
                            <td>{{ stat_list['attackdamage'] + stat_list['attackdamageperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">공격 속도</th>
                            <td>{{ stat_list['attackspeed'] }}</td>
                            <td>{{ stat_list['attackspeedperlevel'] }}</td>
                            <td>{{ stat_list['attackspeed'] + stat_list['attackspeedperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">방어력</th>
                            <td>{{ stat_list['armor'] }}</td>
                            <td>{{ stat_list['armorperlevel'] }}</td>
                            <td>{{ stat_list['armor'] + stat_list['armorperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">마법저항력</th>
                            <td>{{ stat_list['spellblock'] }}</td>
                            <td>{{ stat_list['spellblockperlevel'] }}</td>
                            <td>{{ stat_list['spellblock'] + stat_list['spellblockperlevel'] * 17 }}</td>
                        </tr>
                        <tr>
                        <th scope="row">사거리</th>
                            <td>{{ stat_list['attackrange'] }}</td>
                            <td>{{ stat_list['attackrange'] }}</td>
                            <td>{{ stat_list['attackrange'] }}</td>
                        </tr>
                        <tr>
                        <th scope="row">이동 속도</th>
                            <td>{{ stat_list['movespeed'] }}</td>
                            <td>{{ stat_list['movespeed'] }}</td>
                            <td>{{ stat_list['movespeed'] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="spell-div" id="app">
                <table class="spell-table">
                    <thead>
                        <tr>
                        <th colspan = "6">챔피언 스킬 정보</th>
                        </tr>
                    </thead>
                    <tbody v-cloak>
                        <th>패시브</th>
                        <th>Q</th>
                        <th>W</th>
                        <th>E</th>
                        <th>R</th>
                        <tr @mouseover="updateSkillInfoimg($event)">
                            <!--
                            <td id="0"><img :src=spell_imgURL[0]></td>
                            <td id="1"><img :src=spell_imgURL[1]></td>
                            <td id="2"><img :src=spell_imgURL[2]></td>
                            <td id="3"><img :src=spell_imgURL[3]></td>
                            <td id="4"><img :src=spell_imgURL[4]></td>
                            -->
                            <td><img id="0" :src=spell_imgURL[0]></td>
                            <td><img id="1" :src=spell_imgURL[1]></td>
                            <td><img id="2" :src=spell_imgURL[2]></td>
                            <td><img id="3" :src=spell_imgURL[3]></td>
                            <td><img id="4" :src=spell_imgURL[4]></td>
                        </tr>
                        <tr @mouseover="updateSkillInfo($event)">
                            <td id="0">{{ spell_list[0] }}</td>
                            <td id="1">{{ spell_list[1] }}</td>
                            <td id="2">{{ spell_list[2] }}</td>
                            <td id="3">{{ spell_list[3] }}</td>
                            <td id="4">{{ spell_list[4] }}</td>
                        </tr>
                        <tr>
                            <td v-bind:id="result" colspan="5" style:height="100px">{{ spell_content[result] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div style="height:300px">
                {{ test_list }}
            </div>
            
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'championInfo',
    props: ['selected_champion'],
    data() {
        return {
            champion_square: "data:image/png;base64,",
            test_list: [],
            info_list: [],
            stat_list: [],
            spell_list: [],
            spell_content: [],
            spell_imgURL: [],
            result: ' ',
        }
    },
    created: function () {
        let path = "http://localhost:5000/riot/championinfo?championinfo=";
        path += this.$route.query.championinfo;
        console.log(path)
        axios.get(path).then((res) => {
            this.info_list = res.data[0];
            this.stat_list = res.data[1];
            this.spell_list = res.data[2];
            this.spell_content = res.data[3];
            this.spell_imgURL = res.data[4]
            this.champion_square += this.info_list[2];
            console.log(this.spell_imgURL);
        }).catch((error) => {
            console.error(error);
        });
    },
    mounted() {
        
    },
    methods: {
        updateSkillInfo: function(event) {
            const targetId = event.target.id;
            this.result = targetId
        },
        updateSkillInfoimg: function(event) {
            const targetId = event.target.id;
            this.result = targetId
        },
    }
}
</script>