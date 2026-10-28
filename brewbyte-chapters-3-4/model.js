/* Pure simulation and progress rules, shared by the UI and regression checks. */
'use strict';
window.BrewByteModel = (() => {
  const blankMission = () => ({form:{},pre:'',reflection:'',activity:false,activityNote:'',ai:null,aiShown:false,quiz:null,quizAnswers:{},completed:false});
  const fresh = () => ({version:1,alias:'',role:'Technology lead',missions:{},updated:null});
  function normalize(raw, ids) {
    const state=fresh();
    if (!raw || raw.version!==1 || typeof raw!=='object') return state;
    state.alias=typeof raw.alias==='string'?raw.alias.slice(0,60):'';
    if (['Technology lead','Security analyst','Operations manager','Evidence reporter'].includes(raw.role)) state.role=raw.role;
    state.updated=typeof raw.updated==='string'?raw.updated:null;
    for (const id of ids) {
      const source=raw.missions?.[id];
      if (!source || typeof source!=='object') continue;
      const m=blankMission();
      for (const field of ['pre','reflection','activityNote']) if(typeof source[field]==='string')m[field]=source[field].slice(0,12000);
      for (const field of ['activity','aiShown','completed'])m[field]=source[field]===true;
      m.ai=source.ai===true?true:null;
      m.quiz=source.quiz===true?true:null;
      for (const [key,value] of Object.entries(source.form||{})) if (/^[a-zA-Z0-9_-]{1,50}$/.test(key) && ['string','number','boolean'].includes(typeof value)) m.form[key]=typeof value==='string'?value.slice(0,12000):value;
      for (const [key,value] of Object.entries(source.quizAnswers||{})) if (/^\d+$/.test(key)&&Number.isInteger(value)&&value>=0&&value<5)m.quizAnswers[key]=value;
      // Completion is a learning record, not secure or authenticated grading evidence.
      m.completed=m.completed&&ready(m);
      state.missions[id]=m;
    }
    return state;
  }
  function ready(m) {return !!(m.activity && m.ai && m.quiz && m.pre.trim().length>=20 && m.reflection.trim().length>=60);}
  function seconds(gb,mbps,usable=80) {
    if(!Number.isFinite(gb)||!Number.isFinite(mbps)||!Number.isFinite(usable)||gb<=0||mbps<=0||usable<=0||usable>100)return null;
    return gb*8000/(mbps*usable/100);
  }
  function evaluate(plan,scenario,usable=80) {
    const minutes=seconds(6,plan.up,usable)/60;
    return {minutes,cost:plan.cost<=scenario.budget,deadline:plan.days<=scenario.days,upload:minutes<=scenario.window,eligible:plan.cost<=scenario.budget&&plan.days<=scenario.days&&minutes<=scenario.window};
  }
  function firewall(source,destination,protocol) {
    return (source==='checkout' && destination==='order-api' && protocol==='HTTPS') || (source==='guest' && destination==='internet' && protocol==='HTTPS');
  }
  function quizScore(answers,questions) {return questions.reduce((n,q,i)=>n+(Number.isInteger(answers[i])&&answers[i]===q[2]?1:0),0);}
  return {blankMission,fresh,normalize,ready,seconds,evaluate,firewall,quizScore};
})();
