#define MAX_STEPS 100
#define MAX_DIST 100.
#define SURF_DIST .001

float sdCapsule(float3 p, float3 a, float3 b, float r) {
	float3 ab = b-a;
    float3 ap = p-a;
    
    float t = dot(ab, ap) / dot(ab, ab);
    t = clamp(t, 0., 1.);
    
    float3 c = a + t*ab;
    
    return length(p-c)-r;
}

float sdCylinder(float3 p, float3 a, float3 b, float r) {
	float3 ab = b-a;
    float3 ap = p-a;
    
    float t = dot(ab, ap) / dot(ab, ab);
    //t = clamp(t, 0., 1.);
    
    float3 c = a + t*ab;
    
    float x = length(p-c)-r;
    float y = (abs(t-.5)-.5)*length(ab);
    float e = length(max(float2(x, y), 0.));
    float i = min(max(x, y), 0.);
    
    return e+i;
}

float sdTorus(float3 p, float2 r) {
	float x = length(p.xz)-r.x;
    return length(float2(x, p.y))-r.y;
}

float dBox(float3 p, float3 s) {
	return length(max(abs(p)-s, 0.));
}


float GetDist(float3 p) {
	float4 s = float4(0, 1, 6, 1);
    
    float sphereDist =  length(p-s.xyz)-s.w;
    float planeDist = p.y;
    
    float cd = sdCapsule(p, float3(3, .5, 6), float3(3, 2.5, 6), .5); 
    float td = sdTorus(p-float3(0,.5,6), float2(1.5, .4));
    float bd = dBox(p-float3(-3.5, 1, 6), float3(1,.75,1));
    float cyld = sdCylinder(p, float3(0, .3, 3), float3(3, .3, 5), .3);
    
    float d = min(cd, planeDist);
    d = min(d, td);
    d = min(d, bd);
    
    d = min(d, cyld);
    
    return d;
}

float RayMarch(float3 ro, float3 rd) {
	float dO=0.;
    
    for(int i=0; i<MAX_STEPS; i++) {
    	float3 p = ro + rd*dO;
        float dS = GetDist(p);
        dO += dS;
        if(dO>MAX_DIST || dS<SURF_DIST) break;
    }
    
    return dO;
}

float3 GetNormal(float3 p) {
	float d = GetDist(p);
    float2 e = float2(.001, 0);
    
    float3 n = d - float3(
        GetDist(p-e.xyy),
        GetDist(p-e.yxy),
        GetDist(p-e.yyx));
    
    return normalize(n);
}

float GetLight(float3 p) {
    float3 lightPos = float3(0, 5, 6);
    lightPos.xz += float2(sin(iTime), cos(iTime))*2.;
    float3 l = normalize(lightPos-p);
    float3 n = GetNormal(p);
    
    float dif = clamp(dot(n, l), 0., 1.);
    float d = RayMarch(p+n*SURF_DIST*2., l);
    if(d<length(lightPos-p)) dif *= .1;
    
    return dif;
}

void mainImage( out float4 fragColor, in float2 fragCoord )
{
    float2 uv = (fragCoord-.5*iResolution.xy)/iResolution.y;

    float3 col = float3(0);
    
    float3 ro = float3(0, 2, 0);
    float3 rd = normalize(float3(uv.x-.15, uv.y-.2, 1));

    float d = RayMarch(ro, rd);
    
    float3 p = ro + rd * d;
    
    float dif = GetLight(p);
    col = float3(dif);
    
    col = pow(col, float3(.4545));	// gamma correction
    
    fragColor = float4(col,1.0);
}