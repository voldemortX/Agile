<template>
    <div>
        <!-- page -->
        <el-container width="200px">
            <el-header style="text-align: center; vertical-align:middle;font-size: 40px;height:100px">
                <el-row></el-row>
                <span>{{systemname}}</span>

            </el-header>
            <el-main style="text-align: center; background-color:#000000">
                <el-row>
                    <el-radio-group v-model="method">
                        <el-radio :label="0">相乘法</el-radio>
                        <el-radio :label="1">矩阵法</el-radio>
                    </el-radio-group>
                </el-row>
                <el-row>
                    <el-button name="calc" type="primary" @click.native="calcClick">提交</el-button>
                </el-row>
            </el-main>
            <el-main style="text-align: center">
                <el-tabs v-model="activeName" @tab-click.native="handleClick">
                    <el-tab-pane label="评估准备" name="first">
                        <el-divider content-position="left">评估目标</el-divider>
                        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="aim"></el-input>
                        <el-divider content-position="left">评估范围</el-divider>
                        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="range"></el-input>
                        <el-divider content-position="left">组建团队成员</el-divider>
                        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="team"></el-input>
                    </el-tab-pane>
                    <el-tab-pane label="资产评估" name="second">
                        <div style="float:left">
                            <el-button type="add" @click.native="assetDialogVisible = true">添加</el-button>
                        </div>
                        <el-table :data="tableAsset" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                            <el-table-column prop="asset" label="资产名称" width="260">
                            </el-table-column>
                            <el-table-column prop="integrity" label="完整性" width="140">
                            </el-table-column>
                            <el-table-column prop="availability" label="可用性" width="140">
                            </el-table-column>
                            <el-table-column prop="confidentiality" label="保密性" width="140">
                            </el-table-column>
                            <el-table-column prop="rank" label="资产价值" width="140">
                            </el-table-column>
                            <el-table-column prop="details" label="描述" >
                            </el-table-column>
                            <el-table-column fixed="right" label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button @click.native="formAssetModify(scope.$index)" type="text" size="small" style="font-size:16px;width:38px;height:20px">修改</el-button>
                                    <el-button @click.native="formDelete(scope.$index, tableAsset)" type="text" size="small" style="font-size:16px;width:38px;height:20px">删除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-tab-pane>
                    <el-tab-pane label="脆弱性评估" name="third">
                        <div style="float:left">
                            <el-button type="add" @click.native="vulDialogVisible = true">添加</el-button>
                        </div>
                        <el-table :data="tableVul" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                            <el-table-column prop="vulnerability" label="脆弱性名称" width="260"></el-table-column>
                            <el-table-column prop="rank" label="脆弱性等级" width="140"></el-table-column>
                            <el-table-column prop="vaString" label="资产关联" width="140"></el-table-column>
                            <el-table-column prop="details" label="描述"></el-table-column>
                            <el-table-column fixed="right" label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button @click.native="formVulModify(scope.$index)" type="text" size="small" style="font-size:16px;width:38px;height:20px">修改</el-button>
                                    <el-button @click.native="formDelete(scope.$index, tableVul)" type="text" size="small" style="font-size:16px;width:38px;height:20px">删除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-tab-pane>
                    <el-tab-pane label="威胁评估" name="fourth">
                        <div style="float:left">
                            <el-button type="add" @click.native="threatDialogVisible = true">添加</el-button>
                        </div>
                        <el-table :data="tableThreat" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                            <el-table-column prop="threat" label="威胁名称" width="260"></el-table-column>
                            <el-table-column prop="rank" label="威胁等级" width="140"></el-table-column>
                            <el-table-column prop="tvString" label="威胁的脆弱性关联" width="140"></el-table-column>
                            <el-table-column prop="details" label="描述"></el-table-column>
                        </el-table>
                    </el-tab-pane>
                </el-tabs>
            </el-main>
        </el-container>

        <!-- dialogs -->
        <el-dialog title="添加资产" :visible.sync="assetDialogVisible" :modal-append-to-body="false" :show-close="false">
            <el-form :model="formAsset">
                <el-form-item label="资产名称" :label-width="formLabelWidth">
                    <el-input v-model="formAsset.name" autocomplete="off" width="200px"></el-input>
                </el-form-item>
                <el-form-item label="保密性" :label-width="formLabelWidth">
                    <el-select v-model="formAsset.confidentiality" placeholder="请选择安全等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="完整性" :label-width="formLabelWidth">
                    <el-select v-model="formAsset.integrity" placeholder="请选择安全等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="可用性" :label-width="formLabelWidth">
                    <el-select v-model="formAsset.availability" placeholder="请选择安全等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-input type="textarea" :rows="5" placeholder="请输入资产描述" v-model="formAsset.details"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="dialogAssetClose">取 消</el-button>
                <el-button type="primary" @click.native="formAssertClick">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="添加脆弱性" :visible.sync="vulDialogVisible" :modal-append-to-body="false" :show-close="false">
            <el-form :model="formVul">
                <el-form-item label="脆弱性名称" :label-width="formLabelWidth">
                    <el-input v-model="formVul.name" autocomplete="off" width="200px"></el-input>
                </el-form-item>
                <el-form-item label="脆弱性等级" :label-width="formLabelWidth">
                    <el-select v-model="formVul.rank" placeholder="请选择等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="关联已有资产" :label-width="formLabelWidth">
                    <el-checkbox-group v-model="formVul.va">
                        <el-checkbox v-for="i in tableAsset" :label="i.asset" :key="i.asset">{{i.asset}}</el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item>
                    <el-input type="textarea" :rows="5" placeholder="请输入脆弱性描述" v-model="formVul.details"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="dialogVulClose">取 消</el-button>
                <el-button type="primary" @click.native="formVulClick">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="添加威胁" :visible.sync="threatDialogVisible" :modal-append-to-body="false" :show-close="false">
            <el-form :model="formThreat">
                <el-form-item label="威胁名称" :label-width="formLabelWidth">
                    <el-input v-model="formThreat.name" autocomplete="off" width="200px"></el-input>
                </el-form-item>
                <el-form-item label="威胁等级" :label-width="formLabelWidth">
                    <el-select v-model="formThreat.rank" placeholder="请选择等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="关联已有脆弱性" :label-width="formLabelWidth">
                    <el-checkbox-group v-model="formThreat.tv">
                        <el-checkbox v-for="i in tableVul" :label="i.vulnerability" :key="i.vulnerability">{{i.vulnerability}}</el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item>
                    <el-input type="textarea" :rows="5" placeholder="请输入脆弱性描述" v-model="formThreat.details"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="dialogThreatClose">取 消</el-button>
                <el-button type="primary" @click.native="formThreatClick">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="评估结果" :visible.sync="resultDialogVisible" :modal-append-to-body="false">
            <div slot="title" class="el-dialog__header">
                <h2>评估结果</h2>
                <el-button type="primary" @click.native="createWord">导出</el-button>
                <el-button type="primary" @click.native="createHist">作图</el-button>
            </div>
            <el-table :data="tva_results" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                <el-table-column prop="asset" label="资产名称" width="160"></el-table-column>
                <el-table-column prop="threat" label="威胁名称" width="160"></el-table-column>
                <el-table-column prop="vulnerability" label="脆弱性名称" width="160"></el-table-column>
                <el-table-column prop="level" label="风险等级"></el-table-column>
            </el-table>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="resultDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click.native="submitClick">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog :visible.sync="chartDialogVisible" :modal-append-to-body="false" width="60%">
            <div id="chart" style="width: 1200px;height:400px;"></div>
        </el-dialog>

    </div>
</template>

<script>
    // Matrix method:
    // F[a][v] === level
    const F = [
        [1, 1, 2, 2, 3],
        [1, 1, 2, 3, 4],
        [1, 2, 3, 3, 4],
        [1, 2, 3, 3, 5],
        [2, 2, 4, 5, 5]
    ];
    // L[t][v] === level
    const L = [
        [1, 1, 2, 2, 3],
        [1, 2, 2, 3, 4],
        [1, 2, 3, 3, 4],
        [2, 2, 3, 4, 5],
        [2, 3, 4, 4, 5]
    ];
    // R[f][l] === level
    const R = [
        [1, 1, 2, 2, 3],
        [1, 2, 2, 3, 3],
        [1, 2, 3, 3, 4],
        [2, 2, 3, 4, 4],
        [2, 3, 4, 4, 5]
    ];

    const map = ['很低', '低', '中', '高', '很高'];
    const methods = ['相乘法', '矩阵法'];

    export default {
        name: '_new',
        data() {
            return {
                // Page settings
                activeName: 'first',
                formLabelWidth: '120px',
                assetDialogVisible: false,
                threatDialogVisible: false,
                vulDialogVisible: false,
                resultDialogVisible: false,
                chartDialogVisible: false,

                // Tab data
                aim: '',
                range: '',
                team: '',
                tableAsset: [],
                tableVul: [],
                tableThreat: [],

                // Form data
                formAsset: {
                    name: '',
                    availability: null,
                    integrity: null,
                    confidentiality: null,
                    details: ''
                },
                formThreat: {
                    name: '',
                    rank: null,
                    tv: [],
                    details: ''
                },
                formVul: {
                    name: '',
                    rank: null,
                    va: [],
                    details: ''
                },

                // System data
                systemname: 'test1',
                method: 0,
                tva_results: []

            }
        },

        created () {
            this.systemname = this.$route.query.sysname;
            this.$http({
                method: 'GET',
                url: 'http://134.175.225.180:3000/mock/43/sys/query',
                // url: '/sys/query',
                params: {
                    systemname: this.systemname
                }
            }).then(
                (response) => {
                    // success
                    if (response.ok && response.body.status === 0) {
                        this.loadData(response.body);
                    } else {
                        if(response.body.error !== '该系统不存在')
                            this.messageBox('错误', response.body.error);
                    }
                },
                (error) => {
                    // error?
                    this.messageBox('错误', error.body.error);
                }
            );
        },

        methods: {
            loadData(data) {
                this.method = methods.indexOf(data.method);
                this.tva_results = data.results.tva_results;

                // Parse assets
                for(let i of data.assets)
                {
                    let cia = i.description.split('&&&');
                    let temp = {asset: i.assetname, confidentiality: cia[1], integrity: cia[2],
                        availability: cia[3], details: cia[0], rank: map[i.val - 1]};
                    this.tableAsset.push(temp);
                }

                // Parse vulnerabilities
                for(let i of data.vulnerabilities)
                {
                    let va = data.results.va_results[i.vulname];
                    let temp = {vulnerability: i.vulname, rank: map[i.val - 1],
                        details: i.description, va: va, vaString: va.toString()};
                    this.tableVul.push(temp);
                }

                // Parse threats
                for(let i of data.threats)
                {
                    let tv = data.results.tv_results[i.threatname];
                    let temp = {threat: i.threatname, rank: map[i.val - 1],
                        details: i.description, tv: tv, tvString: tv.toString()};
                    this.tableThreat.push(temp);
                }

                // Parse description
                let str = data.description;
                let temp = str.indexOf('&&&范围：');
                this.aim = str.substr(3, temp - 3);
                str = str.substr(temp + 6, str.length - temp - 6);
                temp = str.indexOf('&&&成员：');
                this.range = str.substr(0, temp);
                str = str.substr(temp + 6, str.length - temp - 6);
                temp = str.indexOf('&&&');
                this.team = str.substr(0, temp);

            },

            levelMultiply(val) {
                // Can't have any malicious values at this point
                return Math.ceil((val - 1) / 5);
            },

            messageBox(title, text) {
                this.$alert(text, title, {
                    confirmButtonText: '确定'
                });
            },

            handleClick(tab, event) {
                console.log(tab, event);
            },

            dialogAssetClose() {
                this.formAsset = {
                    name: '',
                    availability: null,
                    integrity: null,
                    confidentiality: null,
                    details: ''
                };
                this.assetDialogVisible = false;
            },

            dialogVulClose() {
                this.formVul = {
                    name: '',
                    rank: null,
                    va: [],
                    details: ''
                };
                this.vulDialogVisible = false;
            },

            dialogThreatClose() {
                this.formThreat = {
                    name: '',
                    rank: null,
                    tv: [],
                    details: ''
                };
                this.threatDialogVisible = false;
            },

            formAssertClick() {
                if(this.formAsset.name === '' || this.formAsset.confidentiality === null
                    || this.formAsset.integrity === null || this.formAsset.availability === null)
                    this.messageBox('错误提示', '请完整填写必要信息！');
                else {
                    // Calculate val
                    let val = this.formAsset.availability;
                    if (this.formAsset.integrity > val)
                        val = this.formAsset.integrity;
                    if (this.formAsset.confidentiality > val)
                        val = this.formAsset.confidentiality;

                    // Move data
                    let temp = {
                        asset: this.formAsset.name,
                        confidentiality: map[this.formAsset.confidentiality - 1],
                        integrity: map[this.formAsset.integrity - 1],
                        availability: map[this.formAsset.availability - 1],
                        details: this.formAsset.details,
                        rank: map[val - 1]
                    };

                    // Check&Delete
                    for(let i = 0; i < this.tableAsset.length; ++i)
                        if(this.tableAsset[i].asset === temp.asset)
                            this.tableAsset.splice(i, 1);

                    this.tableAsset.push(temp);

                    // Close dialog
                    this.dialogAssetClose();
                }
            },

            formThreatClick() {
                if(this.formThreat.name === '' || this.formThreat.rank === null)
                    this.messageBox('错误提示', '请完整填写必要信息！');
                else
                {
                    // Move data
                    let temp = {
                        threat: this.formThreat.name,
                        tv: this.formThreat.tv,
                        tvString: this.formThreat.tv.toString(),
                        details: this.formThreat.details,
                        rank: map[this.formThreat.rank - 1]
                    };

                    // Check&Delete
                    for(let i = 0; i < this.tableThreat.length; ++i)
                        if(this.tableThreat[i].threat === temp.threat)
                            this.tableThreat.splice(i, 1);

                    this.tableThreat.push(temp);

                    // Close dialog
                    this.dialogThreatClose();
                }
            },

            formVulClick() {
                if(this.formVul.name === '' || this.formVul.rank === null)
                    this.messageBox('错误提示', '请完整填写必要信息！');
                else
                {
                    // Move data
                    let temp = {
                        vulnerability: this.formVul.name,
                        va: this.formVul.va,
                        vaString: this.formVul.va.toString(),
                        details: this.formVul.details,
                        rank: map[this.formVul.rank - 1]
                    };

                    // Check&Delete
                    for(let i = 0; i < this.tableVul.length; ++i)
                        if(this.tableVul[i].vulnerability === temp.vulnerability)
                            this.tableVul.splice(i, 1);

                    this.tableVul.push(temp);

                    // Close dialog
                    this.dialogVulClose();
                }
            },

            formAssetModify(index) {
                // Fill data
                this.formAsset.name = this.tableAsset[index].asset;
                this.formAsset.details = this.tableAsset[index].details;
                this.formAsset.confidentiality = String(map.indexOf(this.tableAsset[index].confidentiality) + 1);
                this.formAsset.integrity = String(map.indexOf(this.tableAsset[index].integrity) + 1);
                this.formAsset.availability = String(map.indexOf(this.tableAsset[index].availability) + 1);

                // Open the same dialog as ADD
                this.assetDialogVisible = true;

            },

            formVulModify(index) {
                // Fill data
                this.formVul.name = this.tableVul[index].vulnerability;
                this.formVul.details = this.tableVul[index].details;
                this.formVul.rank = String(map.indexOf(this.tableVul[index].rank) + 1);
                this.formVul.va = this.tableVul[index].va;

                // Open the same dialog as ADD
                this.vulDialogVisible = true;
            },

            formThreatModify(index) {
                // Fill data
                this.formThreat.name = this.tableThreat[index].threat;
                this.formThreat.details = this.tableThreat[index].details;
                this.formThreat.rank = String(map.indexOf(this.tableThreat[index].rank) + 1);
                this.formThreat.tv = this.tableThreat[index].tv;

                // Open the same dialog as ADD
                this.threatDialogVisible = true;
            },

            formDelete(index, rows) {
                rows.splice(index, 1);
            },

            calcClick() {
                // Calculate results
                // Expand from v
                this.tva_results = [];
                for(let v of this.tableVul)
                {
                    // Search t
                    for(let t of this.tableThreat)
                    {
                        let flag = false;
                        for(let i of t.tv)
                            if(i === v.vulnerability)
                            {
                                flag = true;
                                break;
                            }

                        if(flag === true)
                        {
                            // Search a
                            for(let a of this.tableAsset)
                            {
                                flag = false;
                                for(let i of v.va)
                                    if(i === a.asset)
                                    {
                                        flag = true;
                                        break;
                                    }

                                if(flag === true)
                                {
                                    // append
                                    let temp = {asset: a.asset, vulnerability: v.vulnerability, threat: t.threat,
                                        level: 0};
                                    if(this.method === 0)  // Multiply
                                    {
                                        let val = Math.sqrt((map.indexOf(a.rank) + 1) * (map.indexOf(v.rank) + 1)) *
                                            Math.sqrt((map.indexOf(v.rank) + 1) * (map.indexOf(t.rank) + 1));
                                        temp.level = this.levelMultiply(val);
                                    }
                                    else  // Matrix
                                        temp.level = R[F[map.indexOf(a.rank)][map.indexOf(v.rank)] - 1][L[map.indexOf(t.rank)][map.indexOf(v.rank)] - 1];

                                    this.tva_results.push(temp);
                                }
                            }
                        }
                    }
                }

                // Show results
                this.resultDialogVisible = true;
            },

            submitClick() {
                // Submit a system to server
                let tempMethod = '相乘法';
                if(this.method === 1)
                    tempMethod = '矩阵法';

                let tempAsset = [];
                let tempThreat = [];
                let tempVul = [];
                let tempResults = {tva_results: this.tva_results, tv_results: {}, va_results: {}};
                for(let i of this.tableAsset)
                {
                    let temp = {assetname: i.asset, val: map.indexOf(i.rank) + 1,
                        description: i.details + '&&&' + i.confidentiality + '&&&' + i.integrity + '&&&' + i.availability + '&&&'};
                    tempAsset.push(temp);
                }
                for(let i of this.tableThreat)
                {
                    tempResults.tv_results[i.threat] = i.tv;
                    let temp = {threatname: i.threat, val: map.indexOf(i.rank) + 1, description: i.details};
                    tempThreat.push(temp);
                }
                for(let i of this.tableVul)
                {
                    tempResults.va_results[i.vulnerability] = i.va;
                    let temp = {vulname: i.vulnerability, val: map.indexOf(i.rank) + 1, description: i.details};
                    tempVul.push(temp);
                }
                this.$http({
                    method: 'POST',
                    url: 'http://134.175.225.180:3000/mock/43/sys/submit',
                    // url: '/sys/submit',
                    emulateJSON: true,
                    body: JSON.stringify({
                        systemname: this.systemname,
                        description: '目标：' + this.aim + '&&&范围：' + this.range + '&&&成员：' + this.team + '&&&',
                        method: tempMethod,
                        assets: tempAsset,
                        threats: tempThreat,
                        vulnerabilities: tempVul,
                        results: tempResults
                    })
                }).then(
                    (response) => {
                        // success
                        if (response.ok && response.body.status === 0) {
                            this.messageBox('提示', '结果已提交至服务器');
                        } else {
                            this.messageBox('提交错误', response.body.error);
                        }
                    },
                    (error) => {
                        // error?
                        this.messageBox('提交错误', error.body.error);
                    }
                );
                this.resultDialogVisible = false;
            },

            // Create a table in .docx
            createTable(doc, title, data, tableMap, tableMapCh, tableParaSize) {
                const titleResults = new Paragraph(title).title();
                const tableResults = new Table(data.length + 1, tableMap.length);
                tableResults.setWidth(WidthType.PERCENTAGE, '100%');
                // headers
                for(let i = 0; i < tableMapCh.length; ++i)
                    tableResults.getCell(0, i)
                        .addContent(new Paragraph().center().addRun((new TextRun(tableMapCh[i]).size(tableParaSize))));
                // data
                for(let i = 0; i < data.length; ++i)
                    for(let j = 0; j < tableMap.length; ++j)
                    {
                        const temp = new Paragraph();
                        temp.addRun(new TextRun(data[i][tableMap[j]]).size(tableParaSize));
                        const cell = tableResults.getCell(i + 1, j);
                        cell.addContent(temp);
                    }

                doc.addParagraph(titleResults);
                doc.addParagraph(tableResults);
            },

            createWord() {
                // Definitions
                const spacing = new Paragraph();
                const tvaMap = ['asset', 'vulnerability', 'threat', 'level'];
                const tvaMapCh = ['资产名称', '脆弱性名称', '威胁名称', '风险等级'];
                const assetMap = ['asset', 'confidentiality', 'integrity', 'availability', 'rank', 'details'];
                const assetMapCh = ['资产名称', '保密性', '完整性', '可用性', '最高安全等级', '描述'];
                const vulMap = ['vulnerability', 'vaString', 'rank', 'details'];
                const vulMapCh = ['脆弱性名称', '资产关联', '脆弱性等级', '描述'];
                const threatMap = ['threat', 'tvString', 'rank', 'details'];
                const threatMapCh = ['威胁名称', '脆弱性关联', '威胁等级', '描述'];
                const tableParaSize = 28;
                const paraSize = 32;

                // Descriptions
                const paragraphName = new Paragraph().addRun(new TextRun('系统名：' + this.systemname).size(paraSize));
                const paragraphMethod = new Paragraph().addRun(new TextRun('方法：' + methods[this.method]).size(paraSize));
                const paragraphAim = new Paragraph().addRun(new TextRun('目标：' + this.aim).size(paraSize));
                const paragraphRange = new Paragraph().addRun(new TextRun('范围：' + this.range).size(paraSize));
                const paragraphTeam = new Paragraph().addRun(new TextRun('团队：' + this.team).size(paraSize));

                // Construct document
                const doc = new Document();
                doc.addParagraph(paragraphName);
                doc.addParagraph(paragraphMethod);
                doc.addParagraph(paragraphAim);
                doc.addParagraph(paragraphRange);
                doc.addParagraph(paragraphTeam);
                doc.addParagraph(spacing);
                this.createTable(doc, '资产情况：', this.tableAsset, assetMap, assetMapCh, tableParaSize);
                this.createTable(doc, '脆弱性情况：', this.tableVul, vulMap, vulMapCh, tableParaSize);
                this.createTable(doc, '威胁情况：', this.tableThreat, threatMap, threatMapCh, tableParaSize);
                doc.addParagraph(spacing);
                this.createTable(doc, '评估结果：', this.tva_results, tvaMap, tvaMapCh, tableParaSize);

                // Export
                const packer = new Packer();

                packer.toBlob(doc).then(blob => {
                    saveAs(blob, this.systemname + '评估报告.docx');
                });
            },

            createHist()
            {
                this.chartDialogVisible = true;
                this.$nextTick(function () {
                    // Imports
                    let echarts = require('echarts/lib/echarts');
                    require('echarts/lib/chart/bar');
                    require('echarts/lib/component/tooltip');
                    require('echarts/lib/component/title');

                    // Find DOM
                    let myChart = echarts.init(document.getElementById('chart'));

                    // Define histogram
                    let histOptions = {
                        title: {
                            text: '重要资产的风险值等级柱状图'
                        },
                        tooltip: {},
                        xAxis: {
                            data: []
                        },
                        yAxis: {},
                        axisLabel: {
                            interval:0,
                            rotate:40
                        },
                        series: [{
                            type: 'bar',
                            data: []
                        }]
                    };

                    // Construct bars & Calculate indices
                    let levels = [];
                    let assets = [];
                    let indices = [];
                    let xAxis = [];
                    let total = 0;
                    for(let i of this.tableAsset)
                    {
                        assets.push(i.asset);
                        let count = 0;
                        for(let j of this.tva_results)
                            if(j.asset === i.asset)
                            {
                                levels.push(j.level);
                                xAxis.push('');
                                ++count;
                            }

                        ++count;
                        levels.push(0);
                        xAxis.push('');
                        indices.push(Math.floor(count / 2) + total - 1);
                        total += count;
                    }

                    // Rearrange xAxis
                    for(let i = 0; i < assets.length; ++i)
                        xAxis[indices[i]] = assets[i];

                    // Draw
                    histOptions.xAxis.data = xAxis;
                    histOptions.series[0].data = levels;
                    myChart.setOption(histOptions);

                });
            }

        }
    };
</script>


<style scoped>
    .el-button{
        width:74px;
        height:40px;
        font-size:17px;
    }
</style>
<style>
    .el-header {
        background-color: #000000;
        color: #FFFFFF;
        line-height: 70px;
    }
    .el-main {
        background-color:#FFFFFF;
    }
</style>
