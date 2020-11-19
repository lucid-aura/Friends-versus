<template style="background-color:#000000">
    <div class="custom-home">
        <div>
            <div>챔피언 상세정보</div>
            <table class="champion-info">
                <thead>
                    <tr>
                        <td>{{ this.$route.query.champ }}</td>
                        <td>여명의 성위</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>챔피언 아이콘</td>
                        <td rowspan = "2">챔피언 스킨</td>
                    </tr>
                    <tr>
                        <td>챔피언 tags</td>
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
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">체력 재생</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">마나</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">마나 재생</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">공격력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">공격 속도</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">방어력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">마법저항력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">사거리</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">이동 속도</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="skill-div" id="app">
                <table class="skill-table">
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
                        <tr @mouseover="updateSkillInfo($event)" v-for="(skill, index) in skill_list" :key="index">
                            <td id="P">{{skill.P}}</td>
                            <td id="Q">{{skill.Q}}</td>
                            <td id="W">{{skill.W}}</td>
                            <td id="E">{{skill.E}}</td>
                            <td id="R">{{skill.R}}</td>
                        </tr>
                        <tr>
                            <td v-bind:id="result" colspan="5" style:height="100px">{{skill_list[0][result]}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'championInfo',
    props: ['selected_champion'],
    data() {
        return {
            result: ' ',
            skill_list: [],
            icons: [
                {
                    'icon': 'mdi-checkbox-blank-outline',
                    'class': '',
                    'style': 'text-decoration:none;color:unset;'
                },
                {
                    'icon': 'mdi-checkbox-mark-outline',
                    'class': 'v-icon-highlighted',
                    'style': 'text-decoration:line-through;color:#adb7bbd1;'
                },
                {
                    'icon': 'mdi-close',
                    'class': '',
                    'style': ''
                },
                {
                    'icon': 'mdi-plus',
                    'class': 'v-icon-highlighted',
                    'style': ''
                },
                {
                    'icon': 'mdi-refresh',
                    'class': 'v-icon-highlighted pl-1 pb-1',
                    'style': ''
                }
            ],
            icon_list: []
        }
    },
    created: function () {
        this.fetchDefaults();
    },
    methods: {
        updateSkillInfo: function(event) {
            const targetId = event.target.id;
            this.result = targetId
        },
        fetchDefaults: function () {

            this.skill_list = [
                {
                    'P': '반짝반짝!',
                    'Q': '통통별',
                    'W': '주문도둑',
                    'E': '헤롱헤롱쿨쿨방울',
                    'R': '차원 넘기'
                }
            ];

            this.icons_list = [];
            for (var i = 0; i < this.skill_list.length; i++) {
                if (this.skill_list[i].missing == true) {
                    this.icons_list.push(this.icons[0]);
                } else {
                    this.icons_list.push(this.icons[1]);
                }
            }
        },

        removeRow: function (index) {
            this.skill_list.splice(index, 1);
            this.icons_list.splice(index, 1);
        },

        addRow: function () {
            this.skill_list.push({
                P : '',
                Q : '',
                W : '',
                E : '',
                R : ''
            });
            this.icons_list.push(this.icons[0]);
        },
        checkRow: function (index) {
            if (this.icons_list[index].icon == this.icons[0].icon) {
                this.icons_list[index] = this.icons[1];
                this.skill_list[index].missing = false;
            } else {
                this.icons_list[index] = this.icons[0];
                this.skill_list[index].missing = true;
            }
        },
    }
}
</script>