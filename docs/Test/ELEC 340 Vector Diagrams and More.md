## ELEC 340 Vector Diagrams and More <Badge text="Cool_Tags" type="warn" /> 

### 3D vector plot Cart

```LaTeX
/documentclass[tikz,border=1cm]{standalone} 
/usepackage{tikz-3dplot} 
/begin{document}

/tdplotsetmaincoords{60}{120} 
/begin{tikzpicture} [scale=3, tdplot_main_coords, axis/.style={->,blue,thick}, 
vector/.style={-stealth,red,very thick}, 
vector guide/.style={dashed,red,thick}]

%standard tikz coordinate definition using x, y, z coords
/coordinate (O) at (0,0,0);

%tikz-3dplot coordinate definition using x, y, z coords

/pgfmathsetmacro{/ax}{0.8}
/pgfmathsetmacro{/ay}{0.8}
/pgfmathsetmacro{/az}{0.8}

/coordinate (P) at (/ax,/ay,/az);

%draw axes
/draw[axis] (0,0,0) -- (1,0,0) node[anchor=north east]{$x$};
/draw[axis] (0,0,0) -- (0,1,0) node[anchor=north west]{$y$};
/draw[axis] (0,0,0) -- (0,0,1) node[anchor=south]{$z$};

%draw a vector from O to P
/draw[vector] (O) -- (P);

%draw guide lines to components
/draw[vector guide]         (O) -- (/ax,/ay,0);
/draw[vector guide] (/ax,/ay,0) -- (P);
/draw[vector guide]         (P) -- (0,0,/az);
/draw[vector guide] (/ax,/ay,0) -- (0,/ay,0);
/draw[vector guide] (/ax,/ay,0) -- (0,/ay,0);
/draw[vector guide] (/ax,/ay,0) -- (/ax,0,0);
/node[tdplot_main_coords,anchor=east]
at (/ax,0,0){(/ax, 0, 0)};
/node[tdplot_main_coords,anchor=west]
at (0,/ay,0){(0, /ay, 0)};
/node[tdplot_main_coords,anchor=south]
at (0,0,/az){(0, 0, /az)};
/end{tikzpicture}
/end{document}
```

<hr />



### 3D vector plot Sphere

```LaTeX
/documentclass[tikz]{standalone}
/usepackage{tikz-3dplot}
/begin{document}

/tdplotsetmaincoords{60}{120}

/newcommand{/Prho}{.8}%
/newcommand{/Ptheta}{55}%
/newcommand{/Pphi}{60}%

/begin{tikzpicture}
    [scale=3,
    tdplot_main_coords,
    axis/.style={->,blue,thick},
    vector/.style={-stealth,red,very thick},
    vector guide/.style={dashed,red,thick}]

%standard tikz coordinate definition using x, y, z coords
/coordinate (O) at (0,0,0);

%tikz-3dplot coordinate definition using r, theta, phi coords
/tdplotsetcoord{P}{/Prho}{/Ptheta}{/Pphi}

%draw axes
/draw[axis] (0,0,0) -- (1,0,0) node[anchor=north east]{$x$};
/draw[axis] (0,0,0) -- (0,1,0) node[anchor=north west]{$y$};
/draw[axis] (0,0,0) -- (0,0,1) node[anchor=south]{$z$};

%draw a vector from O to P
/draw[vector] (O) -- (P);

%draw guide lines to components
/draw[vector guide] (O) -- (Pxy);
/draw[vector guide] (Pxy) -- (P);

% Compute x,y,z
/pgfmathsetmacro{/PxCoord}{/Prho * sin(/Pphi) * cos(/Ptheta)}%
/pgfmathsetmacro{/PyCoord}{/Prho * sin(/Pphi) * sin(/Ptheta)}%
/pgfmathsetmacro{/PzCoord}{/Prho * cos(/Pphi)}%

/draw[vector guide, black] (Pxy) -- (Px) node [left]  {/PxCoord};
/draw[vector guide, black] (Pxy) -- (Py) node [above right] {/PyCoord};

/draw[vector guide, magenta] (P) -- (Pxz) node [left]  {/PxCoord};
/draw[vector guide, magenta] (P) -- (Pyz) node [right] {/PyCoord};

/end{tikzpicture}
/end{document}
```

<hr />



### 3D vector plot cart no label

```LaTeX
% https://tex.stackexchange.com/questions/164155/2d-and-3d-vectors-in-tikz
/documentclass[tikz]{standalone}
/usepackage{tikz-3dplot}
/begin{document}

/tdplotsetmaincoords{60}{120}
/begin{tikzpicture}
    [scale=3,
    tdplot_main_coords,
    axis/.style={->,blue,thick},
    vector/.style={-stealth,red,very thick},
    vector guide/.style={dashed,red,thick}]

%standard tikz coordinate definition using x, y, z coords
/coordinate (O) at (0,0,0);

%tikz-3dplot coordinate definition using r, theta, phi coords
/tdplotsetcoord{P}{.8}{55}{60}

%draw axes
/draw[axis] (0,0,0) -- (1,0,0) node[anchor=north east]{$x$};
    /draw[axis] (0,0,0) -- (0,1,0) node[anchor=north west]{$y$};
    /draw[axis] (0,0,0) -- (0,0,1) node[anchor=south]{$z$};

%draw a vector from O to P
/draw[vector] (O) -- (P);

%draw guide lines to components
/draw[vector guide] (O) -- (Pxy);
/draw[vector guide] (Pxy) -- (P);
/end{tikzpicture}
/end{document}

and see

/documentclass{article}
/usepackage[pdftex,active,tightpage]{preview}
/setlength/PreviewBorder{2mm}
/usepackage{tikz}
/usepackage{tikz-3dplot}

/begin{document}
/begin{preview}
	/tdplotsetmaincoords{70}{110}

	/begin{tikzpicture}[scale=3,tdplot_main_coords]
		/draw[thick,->] (0,0,0) -- (1,0,0) node[anchor=north east]{$x$};
		/draw[thick,->] (0,0,0) -- (0,1,0) node[anchor=north west]{$y$};
		/draw[thick,->] (0,0,0) -- (0,0,1) node[anchor=south]{$z$};
		/tdplotsetcoord{O}{0}{0}{0}
		/tdplotsetcoord{P}{.8}{50}{70}

		%draw a vector from origin to point (P)
		/draw[-stealth,color=red] (O) -- (P);

		%draw projection on xy plane, and a connecting line
		/draw[dashed, color=red] (O) -- (Pxy);
		/draw[dashed, color=red] (P) -- (Pxy);
		/tdplotsetthetaplanecoords{70}
		/draw[tdplot_rotated_coords,color=blue,thick,->] (0,0,0)
		-- (.2,0,0) node[anchor=east]{$x'$};
		/draw[tdplot_rotated_coords,color=blue,thick,->] (0,0,0)
		-- (0,.2,0) node[anchor=north]{$y'$};
		/draw[tdplot_rotated_coords,color=blue,thick,->] (0,0,0)
		-- (0,0,.2) node[anchor=west]{$z'$};
	/end{tikzpicture}
/end{preview}
/end{document}
```

<hr />



### Tower Defence

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ProjectileScript : MonoBehaviour {

	public float damage;                //How much damage will the enemy receive
	public float speed = 1f;            //How fast the projectile moves

	public Vector3 direction;           //What direction the projectile is heading

	public float lifeDuration = 10f;    //How long the projectile lives before self-destructing


	// Initialize the direction, set the right rotation and the timer for self-destruction
	void Start() {
		//Normalize the direction
		direction = direction.normalized;

		//Fix the rotation
		float angle = Mathf.Atan2(-direction.y, direction.x) * Mathf.Rad2Deg;
		transform.rotation = Quaternion.AngleAxis(angle, Vector3.forward);

		//Set the timer for self-destruction
		Destroy(gameObject, lifeDuration);
	}

	// Update the position of the projectile according to time and speed
	void Update() {
		transform.position += direction * Time.deltaTime * speed;
	}
}
```

Creating the tower in unity
```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class standardTOwer : MonoBehaviour {

	//Boolean to check if the tower is upgradable
	public bool isUpgradable = true;

	private int upgradeLevel;        //Level of the Tower
	public Sprite[] upgradeSprites; //Different sprites for the different levels of the Cupcake Tower
	public void Upgrade() {
		//Check if the tower is upgradable
		if (!isUpgradable) {
			return;
		}

		//Increase the level of the tower
		upgradeLevel++;

		//Check if the tower has reached its last level
		if(upgradeLevel < upgradeSprites.Length) {
			isUpgradable = false;
		}

		//Increase the stats of the tower
		rangeRadius += 1f;
		reloadTime -= 0.5f;

		//Change graphics of the tower
		GetComponent<SpriteRenderer>().sprite = upgradeSprites[upgradeLevel];
	}

	public float rangeRadius;           //Maximum distance that the Cupcake Tower can shoot
	public float reloadTime;            //Time before the Cupcake Tower is able to shoot again
	public GameObject projectilePrefab; //Projectile type that is fired from the Cupcake Tower

	private float elapsedTime;          //Time elapsed from the last time the Cupcake Tower has shot

	//Implements the shooting logic
	void Update () {
		if (elapsedTime >= reloadTime) {
			//Reset elapsed Time
			elapsedTime = 0;

			//Find all the gameObjects with a collider within the range of the Cupcake Tower
			Collider2D[] hitColliders = Physics2D.OverlapCircleAll(transform.position, rangeRadius);

			//Check if there is at least one gameObject found
			if (hitColliders.Length != 0) {
				//Loop over all the gameObjects to identify the closest to the Cupcake Tower
				float min = int.MaxValue;
				int index = -1;

				for (int i = 0; i < hitColliders.Length; i++) {
					if (hitColliders[i].tag == "Enemy") {
						float distance = Vector2.Distance(hitColliders[i].transform.position, transform.position);
						if (distance < min) {
							index = i;
							min = distance;
						}
					}
				}
				if (index == -1)
					return;

				//Get the direction of the target
				Transform target = hitColliders[index].transform;
				Vector2 direction = (target.position - transform.position).normalized;

				//Create the Projectile
				GameObject projectile = GameObject.Instantiate(projectilePrefab, transform.position, Quaternion.identity) as GameObject;
				projectile.GetComponent<ProjectileScript>().direction = direction;
			}
		}
		elapsedTime += Time.deltaTime;
	}

	//Function called when the player clicks on the Tower
	void OnMouseDown() {
		//Assign this tower as the active tower for trading operations
		console.log('player clicked on this tower')
		//TradeCupcakeTowers.setActiveTower(this);
	}
}
```

<hr />



### no name

```Python
import time    

start = start = time.time()
with open("test.txt", 'w') as f:
    for i in range(10000000):
        # print('This is a speed test', file=f)
        # f.write('This is a speed test/n')
end = time.time()
print(end - start)
```

<hr />


